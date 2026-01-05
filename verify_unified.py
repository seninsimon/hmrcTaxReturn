from tax_forms.views import generate_unified_pdf_view
from django.test import RequestFactory
import requests
from unittest.mock import MagicMock
import django
import os
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tax_project.settings')
django.setup()


# Mock data from user request
MOCK_DATA = {
    "data": {
        "SA100": {
            "tr1": {},  # Simplified for mock
            "YTR1_1A": "X", "PRO11_1_0": "X"  # Test normalization
        },
        "SA102": [{"EMP1": "Test"}],
        "SA103S": [{"SSE1": "Test"}],
        "SA105": {"PRO1": "Test"},  # As dict
        "SA110": {"CAL1": "Test"}
    }
}


def test_unified_view():
    print("Testing generate_unified_pdf_view...")

    # Mock requests.get
    original_get = requests.get
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_DATA
    mock_response.status_code = 200
    requests.get = MagicMock(return_value=mock_response)

    try:
        factory = RequestFactory()
        request = factory.get('/api/generate/unified/')

        response = generate_unified_pdf_view(request)

        if response.status_code == 200:
            print("Success! PDF generated.")
            print(f"Content-Type: {response['Content-Type']}")
            # Ideally save it to check
            with open('verify_unified_output.pdf', 'wb') as f:
                f.write(b''.join(response.streaming_content))
            print("Saved to verify_unified_output.pdf")
        else:
            print(f"Failed with status {response.status_code}")
            print(response.content)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        requests.get = original_get


if __name__ == "__main__":
    test_unified_view()
