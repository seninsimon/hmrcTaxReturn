from tax_forms.views import generate_sa100_view
from django.test import RequestFactory
import os
import django
from django.conf import settings
import json
import sys

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tax_project.settings")
django.setup()


def test_generate_pdf():
    factory = RequestFactory()

    # Sample data
    data = {
        "tr1": {
            "utr": "1234567890",
            "nino": "QQ123456A"
        }
    }

    request = factory.post(
        '/api/generate/sa100/',
        data=json.dumps(data),
        content_type='application/json'
    )

    print("Testing generate_sa100_view...")
    response = generate_sa100_view(request)

    if response.status_code == 200:
        print("Success! Status code 200")
        if response['Content-Type'] == 'application/pdf':
            print("Content-Type is application/pdf")
            # Consume content to verify it's not empty
            content = b"".join(response.streaming_content)
            print(f"PDF size: {len(content)} bytes")
            if len(content) > 1000:
                print("PDF generated successfully.")
            else:
                print("Warning: PDF seems too small.")
        else:
            print(f"Unexpected Content-Type: {response['Content-Type']}")
    else:
        print(f"Failed! Status code: {response.status_code}")
        # Parse content
        try:
            print(f"Response: {response.content.decode()}")
        except Exception as ex:
            print(f"Could not decode content: {ex}")


if __name__ == "__main__":
    try:
        test_generate_pdf()
    except Exception as e:
        print(f"Error during test: {e}")
        import traceback
        traceback.print_exc()
