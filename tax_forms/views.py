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




# ==========================================
# Unified PDF Generation
# ==========================================


def normalize_keys(data_dict):
    ##example  PRO11_1_0 = PRO11.1_0 
    import re
    new_dict = {}


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
