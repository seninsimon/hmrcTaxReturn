from tax_forms.views import generate_sa102_view
from django.test import RequestFactory
import os
import django
from django.conf import settings
import json
import sys

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tax_project.settings")
django.setup()


def test_generate_sa102():
    factory = RequestFactory()

    # Sample data for SA102
    data = {
        "p1": {
            "pay_from_this_employment": "50000",
            "tax_taken_off_pay": "10000"
        }
    }

    request = factory.post(
        '/api/generate/sa102/',
        data=json.dumps(data),
        content_type='application/json'
    )

    print("Testing generate_sa102_view...")
    response = generate_sa102_view(request)

    if response.status_code == 200:
        print("Success! Status code 200")
        if response['Content-Type'] == 'application/pdf':
            print("Content-Type is application/pdf")
            content = response.content
            print(f"PDF size: {len(content)} bytes")
        else:
            print(f"Unexpected Content-Type: {response['Content-Type']}")
    else:
        print(f"Failed! Status code: {response.status_code}")
        try:
            print(f"Response: {response.content.decode()}")
        except Exception as ex:
            print(f"Could not decode content: {ex}")


if __name__ == "__main__":
    try:
        test_generate_sa102()
    except Exception as e:
        print(f"Error during test: {e}")
