from tax_forms.form_definitions.sa110.mappings import SA110_TC1, SA110_TC2
from tax_forms.form_definitions.sa105.mappings import SA105_UKP1, SA105_UKP2
from tax_forms.form_definitions.sa103s.mappings import SA103s_SES1, SA103s_SES2
from pypdf import PdfWriter
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
    url = "http://192.168.1.56:8000/api/hmrc/MTR/generate_Data_for_tax_return/"
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


# ==========================================
# Unified PDF Generation
# ==========================================


def normalize_keys(data_dict):
    """
    Recursively normalize keys in the dictionary.
    Converts keys like 'PRO11_1_0' to 'PRO11.1_0' if the dot version is standard.
    Since we don't have a master list of all 'dot' keys easily accessible here without
    importing everything, we will use a heuristic or specific known patterns if needed.

    However, the user specific request was: "some values will be , for example PRO11.1_0 but in the data we will get like PRO11_1_0"

    We will implement a specific fixer for strict matches against known patterns or simply 
    try to replace occurrences of '_1_' with '.1_' and '_2_' with '.2_' etc where appropriate, 
    BUT blindly doing this is dangerous.

    Better approach:
    Flatten the data and check if the key exists in our mappings? No, that's expensive.

    Let's look at the specific examples:
    PRO11_1_0 -> PRO11.1_0
    SSE10_1_0 -> SSE10.1_0

    It seems the pattern is: [LETTERS][NUMBER]_[SUB_NUMBER]_[INDEX] -> [LETTERS][NUMBER].[SUB_NUMBER]_[INDEX]

    We can write a specific replacement logic or just manual overrides for common known issues if the list is small.
    Given the user's specific comment, I will attempt to detect the pattern `[A-Z]+\\d+_\\d+_\\d+` and convert the first underscore to a dot.
    """
    import re
    new_dict = {}

    # Pattern to find keys like PRO11_1_0 (Key_Sub_Index) -> Key.Sub_Index
    # We only want to target keys that look like they should be dots.
    # Mappings have keys like "SSE10.1_0". Data has "SSE10_1_0".

    # Regex for Keys like: (Letters)(Numbers)_(Numbers)_(Numbers) e.g., SSE10_1_0
    # Group 1: Prefix (SSE10), Group 2: First digit part (1), Group 3: Second digit part (0)
    # We want to change the first underscore between Number sets to a dot.

    # Actually, let's just use string replacement for the specific known "dot" fields
    # if we can identify them vs normal fields.
    # But since we want to be generic, let's try a regex approach that seems safe for these forms.
    # Most keys are like "SSE1" or "SSE1_0" (Boxed).
    # Boxed fields with sub-sections are "SSE10.1_0".
    # Incoming data "SSE10_1_0".

    pattern = re.compile(r'^([A-Z]+\d+)_(\d+)_(\d+)$')  # Matches PRO11_1_0

    for k, v in data_dict.items():
        if isinstance(v, dict):
            new_dict[k] = normalize_keys(v)
        elif isinstance(v, list):
            new_dict[k] = [normalize_keys(item) if isinstance(
                item, dict) else item for item in v]
        else:
            # Check pattern
            match = pattern.match(k)
            if match:
                # Convert PRO11_1_0 -> PRO11.1_0
                new_key = f"{match.group(1)}.{match.group(2)}_{match.group(3)}"
                new_dict[new_key] = v
                # Also keep original just in case? No, usually safer to just swap if we are sure.
                # But we might collide if both exist.
            else:
                new_dict[k] = v
    return new_dict


def fetch_unified_data():
    url = "http://192.168.1.56:8000/api/hmrc/MTR/generate_Data_for_tax_return/"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.json().get('data', {})
    except Exception as e:
        print(f"Error fetching unified data: {e}")
        return None


def map_single_form_data(flat_data, mappings_list):
    """
    Maps flat key-value pairs to page-specific dictionaries based on mappings.
    mappings_list: List of tuples ('page_key', mapping_dict)
    """
    mapped_data = {page_key: {} for page_key, _ in mappings_list}

    for key, value in flat_data.items():
        for page_name, page_mapping in mappings_list:
            if key in page_mapping:
                mapped_data[page_name][key] = value
            # Also check for normalized keys if the flat data wasn't normalized perfectly
            # (Though we normalize before calling this currently)

    return mapped_data


@require_http_methods(["GET"])
@csrf_exempt
def generate_unified_pdf_view(request):
    """
    Fetches data for all forms and merges them into a single PDF.
    Does not leave temporary files on disk.
    """
    import tempfile
    import io

    try:
        raw_data = fetch_unified_data()
        if not raw_data:
            return JsonResponse({'error': 'Failed to fetch data from external API'}, status=502)

        # Normalize keys (handle the _ vs . issue)
        data = normalize_keys(raw_data)

        merger = PdfWriter()

        base_dir = settings.BASE_DIR
        # Use a temporary directory context manager to ensure cleanup
        with tempfile.TemporaryDirectory() as output_dir:

            # 1. SA100
            if 'SA100' in data and data['SA100'] and generate_sa100:
                sa100_flat = data['SA100']
                sa100_mappings = [
                    ('tr1', SA100_TR1), ('tr2', SA100_TR2), ('tr3',
                                                             SA100_TR3), ('tr4', SA100_TR4),
                    ('tr5', SA100_TR5), ('tr6', SA100_TR6), ('tr7',
                                                             SA100_TR7), ('tr8', SA100_TR8)
                ]
                sa100_data = map_single_form_data(sa100_flat, sa100_mappings)

                path_sa100 = os.path.join(output_dir, 'sa100.pdf')
                templates_sa100 = os.path.join(
                    base_dir, 'tax_forms', 'form_definitions', 'sa100', 'templates')

                generated_path = generate_sa100(
                    sa100_data, output_path=path_sa100, templates_dir=templates_sa100)
                merger.append(generated_path)

            # 2. SA102 (Employment)
            if 'SA102' in data and data['SA102'] and generate_sa102:
                sa102_list = data['SA102'] if isinstance(
                    data['SA102'], list) else [data['SA102']]
                from tax_forms.form_definitions.sa102.mappings import SA102_TR1, SA102_TR2

                for idx, form_data in enumerate(sa102_list):
                    mapped_sa102 = map_single_form_data(
                        form_data, [('tr1', SA102_TR1), ('tr2', SA102_TR2)])

                    path_sa102 = os.path.join(output_dir, f'sa102_{idx}.pdf')
                    templates_sa102 = os.path.join(
                        base_dir, 'tax_forms', 'form_definitions', 'sa102', 'templates')

                    generated_path = generate_sa102(
                        mapped_sa102, output_path=path_sa102, templates_dir=templates_sa102)
                    merger.append(generated_path)

            # 3. SA103S (Self-Employment Short)
            if 'SA103S' in data and data['SA103S'] and generate_sa103s:
                sa103s_list = data['SA103S'] if isinstance(
                    data['SA103S'], list) else [data['SA103S']]

                for idx, form_data in enumerate(sa103s_list):
                    mapped_sa103s = map_single_form_data(
                        form_data, [('ses1', SA103s_SES1), ('ses2', SA103s_SES2)])

                    path_sa103s = os.path.join(output_dir, f'sa103s_{idx}.pdf')
                    templates_sa103s = os.path.join(
                        base_dir, 'tax_forms', 'form_definitions', 'sa103s', 'templates')

                    generated_path = generate_sa103s(
                        mapped_sa103s, output_path=path_sa103s, templates_dir=templates_sa103s)
                    merger.append(generated_path)

            # 4. SA105 (UK Property)
            if 'SA105' in data and data['SA105'] and generate_sa105:
                sa105_input = data['SA105']
                sa105_list = sa105_input if isinstance(
                    sa105_input, list) else [sa105_input]

                for idx, form_data in enumerate(sa105_list):
                    mapped_sa105 = map_single_form_data(
                        form_data, [('ukp1', SA105_UKP1), ('ukp2', SA105_UKP2)])

                    path_sa105 = os.path.join(output_dir, f'sa105_{idx}.pdf')
                    templates_sa105 = os.path.join(
                        base_dir, 'tax_forms', 'form_definitions', 'sa105', 'templates')

                    generated_path = generate_sa105(
                        mapped_sa105, output_path=path_sa105, templates_dir=templates_sa105)
                    merger.append(generated_path)

            # 5. SA110 (Tax Calculation)
            if 'SA110' in data and data['SA110'] and generate_sa110:
                sa110_input = data['SA110']
                sa110_list = sa110_input if isinstance(
                    sa110_input, list) else [sa110_input]

                for idx, form_data in enumerate(sa110_list):
                    mapped_sa110 = map_single_form_data(
                        form_data, [('tc1', SA110_TC1), ('tc2', SA110_TC2)])

                    path_sa110 = os.path.join(output_dir, f'sa110_{idx}.pdf')
                    templates_sa110 = os.path.join(
                        base_dir, 'tax_forms', 'form_definitions', 'sa110', 'templates')

                    generated_path = generate_sa110(
                        mapped_sa110, output_path=path_sa110, templates_dir=templates_sa110)
                    merger.append(generated_path)

            # Write merged PDF to memory buffer
            buffer = io.BytesIO()
            merger.write(buffer)
            merger.close()
            buffer.seek(0)

            # Temporary directory is cleaned up here when exiting context

        return FileResponse(buffer, content_type='application/pdf', as_attachment=True, filename='hmrc_full_return.pdf')

    except Exception as e:
        print(f"Error in unified generation: {e}")
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)
