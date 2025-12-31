"""
Django Views Example for HMRC Tax Return Generators
Copy this to your Django app's views.py
"""

from django.http import FileResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
import os

from forms.sa100.generator import generate_sa100
from forms.sa102.generator import generate_sa102


@require_http_methods(["POST"])
@csrf_exempt  # Remove in production, use proper CSRF handling
def generate_sa100_view(request):
    """
    Generate SA100 PDF from user data

    POST /api/generate/sa100/
    Body: {
        "tr1": {...},
        "tr2": {...},
        ...
    }

    Returns: PDF file
    """
    try:
        # Parse request data
        data = json.loads(request.body)

        # Generate unique filename
        user_id = getattr(request.user, 'id', 'anonymous')
        output_path = f"media/tax_returns/sa100_{user_id}.pdf"

        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Generate PDF
        pdf_path = generate_sa100(data, output_path=output_path)

        # Return PDF as response
        response = FileResponse(
            open(pdf_path, 'rb'),
            content_type='application/pdf',
            as_attachment=True,
            filename='sa100_completed.pdf'
        )
        return response

    except Exception as e:
        return JsonResponse({
            'error': str(e),
            'form_type': 'SA100'
        }, status=400)


@require_http_methods(["POST"])
@csrf_exempt  # Remove in production, use proper CSRF handling
def generate_sa102_view(request):
    """
    Generate SA102 PDF from user data

    POST /api/generate/sa102/
    Body: {
        "p1": {...}
    }

    Returns: PDF file
    """
    try:
        # Parse request data
        data = json.loads(request.body)

        # Generate unique filename
        user_id = getattr(request.user, 'id', 'anonymous')
        output_path = f"media/tax_returns/sa102_{user_id}.pdf"

        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Generate PDF
        pdf_path = generate_sa102(data, output_path=output_path)

        # Return PDF as response
        response = FileResponse(
            open(pdf_path, 'rb'),
            content_type='application/pdf',
            as_attachment=True,
            filename='sa102_completed.pdf'
        )
        return response

    except FileNotFoundError as e:
        return JsonResponse({
            'error': 'SA102 template not configured',
            'details': str(e)
        }, status=404)

    except Exception as e:
        return JsonResponse({
            'error': str(e),
            'form_type': 'SA102'
        }, status=400)


# Alternative: Combined view with form_type parameter
@require_http_methods(["POST"])
@csrf_exempt
def generate_tax_form_view(request, form_type):
    """
    Generate any tax form based on form_type parameter

    POST /api/generate/<form_type>/
    Examples:
        /api/generate/sa100/
        /api/generate/sa102/
    """
    try:
        data = json.loads(request.body)
        user_id = getattr(request.user, 'id', 'anonymous')

        # Map form types to generators
        generators = {
            'sa100': (generate_sa100, 'sa100_completed.pdf'),
            'sa102': (generate_sa102, 'sa102_completed.pdf'),
        }

        if form_type not in generators:
            return JsonResponse({
                'error': f'Unknown form type: {form_type}',
                'available': list(generators.keys())
            }, status=400)

        generator_func, filename = generators[form_type]
        output_path = f"media/tax_returns/{form_type}_{user_id}.pdf"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        pdf_path = generator_func(data, output_path=output_path)

        return FileResponse(
            open(pdf_path, 'rb'),
            content_type='application/pdf',
            as_attachment=True,
            filename=filename
        )

    except Exception as e:
        return JsonResponse({
            'error': str(e),
            'form_type': form_type
        }, status=400)
