from django.http import FileResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.conf import settings

# Adjust imports to new structure
try:
    from tax_forms.form_definitions.sa100.generator import generate_sa100
    from tax_forms.form_definitions.sa100.test_data import (
        DATA_SA100_TR1, DATA_SA100_TR2, DATA_SA100_TR3,
        DATA_SA100_TR4, DATA_SA100_TR5, DATA_SA100_TR6,
        DATA_SA100_TR7, DATA_SA100_TR8
    )
except ImportError:
    generate_sa100 = None

try:
    from tax_forms.form_definitions.sa102.generator import generate_sa102
    from tax_forms.form_definitions.sa102.test_data import DATA_SA102_TR1, DATA_SA102_TR2
except ImportError:
    generate_sa102 = None

try:
    from tax_forms.form_definitions.sa103s.generator import generate_sa103s
    from tax_forms.form_definitions.sa103s.test_data import DATA_SA103s_SES1, DATA_SA103s_SES2
except ImportError:
    generate_sa103s = None

try:
    from tax_forms.form_definitions.sa105.generator import generate_sa105
    from tax_forms.form_definitions.sa105.test_data import DATA_SA105_UKP1, DATA_SA105_UKP2
except ImportError:
    generate_sa105 = None

try:
    from tax_forms.form_definitions.sa110.generator import generate_sa110
    from tax_forms.form_definitions.sa110.test_data import DATA_SA110_TC1, DATA_SA110_TC2
except ImportError:
    generate_sa110 = None


import requests
from tax_forms.form_definitions.sa100.mappings import (
    SA100_TR1, SA100_TR2, SA100_TR3, SA100_TR4,
    SA100_TR5, SA100_TR6, SA100_TR7, SA100_TR8
)


def fetch_and_map_sa100_data():
    url = "http://192.168.1.49:8000/api/hmrc/MTR/generate_Data_for_tax_return/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        json_data = response.json()
        flat_data = json_data.get('data', {})

        mapped_data = {
            'tr1': {}, 'tr2': {}, 'tr3': {}, 'tr4': {},
            'tr5': {}, 'tr6': {}, 'tr7': {}, 'tr8': {}
        }

        mappings = [
            ('tr1', SA100_TR1), ('tr2', SA100_TR2), ('tr3',
                                                     SA100_TR3), ('tr4', SA100_TR4),
            ('tr5', SA100_TR5), ('tr6', SA100_TR6), ('tr7',
                                                     SA100_TR7), ('tr8', SA100_TR8)
        ]

        for key, value in flat_data.items():
            for page_name, page_mapping in mappings:
                if key in page_mapping:
                    mapped_data[page_name][key] = value

        return mapped_data
    except Exception as e:
        print(f"Error fetching external data: {e}")
        return None


@require_http_methods(["GET", "POST"])
@csrf_exempt
def generate_sa100_view(request):
    """
    Generate SA100 PDF from user data or default test data.
    """
    if not generate_sa100:
        return JsonResponse({'error': 'SA100 generator not available'}, status=501)

    try:
        if request.method == "POST":
            data = json.loads(request.body)
        else:
            # GET request - try to fetch from external API first
            external_data = fetch_and_map_sa100_data()

            if external_data:
                data = external_data
            else:
                # Fallback to local test data if fetch fails
                data = {
                    'tr1': DATA_SA100_TR1,
                    'tr2': DATA_SA100_TR2,
                    'tr3': DATA_SA100_TR3,
                    'tr4': DATA_SA100_TR4,
                    'tr5': DATA_SA100_TR5,
                    'tr6': DATA_SA100_TR6,
                    'tr7': DATA_SA100_TR7,
                    'tr8': DATA_SA100_TR8,
                }

        user = getattr(request, 'user', None)
        user_id = getattr(user, 'id', 'anonymous') if user else 'anonymous'
        media_root = getattr(settings, 'MEDIA_ROOT', 'media')
        output_dir = os.path.join(media_root, 'tax_returns')
        output_path = os.path.join(output_dir, f"sa100_{user_id}.pdf")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        base_dir = settings.BASE_DIR
        templates_dir = os.path.join(
            base_dir, 'tax_forms', 'form_definitions', 'sa100', 'templates')

        pdf_path = generate_sa100(
            data, output_path=output_path, templates_dir=templates_dir)

        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf', as_attachment=True, filename='sa100_completed.pdf')

    except Exception as e:
        return JsonResponse({'error': str(e), 'form_type': 'SA100'}, status=400)


@require_http_methods(["GET", "POST"])
@csrf_exempt
def generate_sa102_view(request):
    """
    Generate SA102 PDF from user data or default test data.
    """
    if not generate_sa102:
        return JsonResponse({'error': 'SA102 generator not available'}, status=501)

    try:
        if request.method == "POST":
            data = json.loads(request.body)
        else:
            data = {
                'tr1': DATA_SA102_TR1,
                'tr2': DATA_SA102_TR2
            }

        user = getattr(request, 'user', None)
        user_id = getattr(user, 'id', 'anonymous') if user else 'anonymous'
        media_root = getattr(settings, 'MEDIA_ROOT', 'media')
        output_dir = os.path.join(media_root, 'tax_returns')
        output_path = os.path.join(output_dir, f"sa102_{user_id}.pdf")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        base_dir = settings.BASE_DIR
        templates_dir = os.path.join(
            base_dir, 'tax_forms', 'form_definitions', 'sa102', 'templates')

        pdf_path = generate_sa102(
            data, output_path=output_path, templates_dir=templates_dir)

        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf', as_attachment=True, filename='sa102_completed.pdf')

    except Exception as e:
        return JsonResponse({'error': str(e), 'form_type': 'SA102'}, status=400)


@require_http_methods(["GET", "POST"])
@csrf_exempt
def generate_sa103s_view(request):
    """
    Generate SA103S PDF from user data or default test data.
    """
    if not generate_sa103s:
        return JsonResponse({'error': 'SA103S generator not available'}, status=501)

    try:
        if request.method == "POST":
            data = json.loads(request.body)
        else:
            data = {
                'ses1': DATA_SA103s_SES1,
                'ses2': DATA_SA103s_SES2
            }

        user = getattr(request, 'user', None)
        user_id = getattr(user, 'id', 'anonymous') if user else 'anonymous'
        media_root = getattr(settings, 'MEDIA_ROOT', 'media')
        output_dir = os.path.join(media_root, 'tax_returns')
        output_path = os.path.join(output_dir, f"sa103s_{user_id}.pdf")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        base_dir = settings.BASE_DIR
        templates_dir = os.path.join(
            base_dir, 'tax_forms', 'form_definitions', 'sa103s', 'templates')

        pdf_path = generate_sa103s(
            data, output_path=output_path, templates_dir=templates_dir)

        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf', as_attachment=True, filename='sa103s_completed.pdf')

    except Exception as e:
        return JsonResponse({'error': str(e), 'form_type': 'SA103S'}, status=400)


@require_http_methods(["GET", "POST"])
@csrf_exempt
def generate_sa105_view(request):
    """
    Generate SA105 PDF from user data or default test data.
    """
    if not generate_sa105:
        return JsonResponse({'error': 'SA105 generator not available'}, status=501)

    try:
        if request.method == "POST":
            data = json.loads(request.body)
        else:
            data = {
                'ukp1': DATA_SA105_UKP1,
                'ukp2': DATA_SA105_UKP2
            }

        user = getattr(request, 'user', None)
        user_id = getattr(user, 'id', 'anonymous') if user else 'anonymous'
        media_root = getattr(settings, 'MEDIA_ROOT', 'media')
        output_dir = os.path.join(media_root, 'tax_returns')
        output_path = os.path.join(output_dir, f"sa105_{user_id}.pdf")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        base_dir = settings.BASE_DIR
        templates_dir = os.path.join(
            base_dir, 'tax_forms', 'form_definitions', 'sa105', 'templates')

        pdf_path = generate_sa105(
            data, output_path=output_path, templates_dir=templates_dir)

        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf', as_attachment=True, filename='sa105_completed.pdf')

    except Exception as e:
        return JsonResponse({'error': str(e), 'form_type': 'SA105'}, status=400)


@require_http_methods(["GET", "POST"])
@csrf_exempt
def generate_sa110_view(request):
    """
    Generate SA110 PDF from user data or default test data.
    """
    if not generate_sa110:
        return JsonResponse({'error': 'SA110 generator not available'}, status=501)

    try:
        if request.method == "POST":
            data = json.loads(request.body)
        else:
            data = {
                'tc1': DATA_SA110_TC1,
                'tc2': DATA_SA110_TC2
            }

        user = getattr(request, 'user', None)
        user_id = getattr(user, 'id', 'anonymous') if user else 'anonymous'
        media_root = getattr(settings, 'MEDIA_ROOT', 'media')
        output_dir = os.path.join(media_root, 'tax_returns')
        output_path = os.path.join(output_dir, f"sa110_{user_id}.pdf")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        base_dir = settings.BASE_DIR
        templates_dir = os.path.join(
            base_dir, 'tax_forms', 'form_definitions', 'sa110', 'templates')

        pdf_path = generate_sa110(
            data, output_path=output_path, templates_dir=templates_dir)

        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf', as_attachment=True, filename='sa110_completed.pdf')

    except Exception as e:
        return JsonResponse({'error': str(e), 'form_type': 'SA110'}, status=400)
