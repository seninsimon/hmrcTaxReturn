from tax_forms.views import (
    generate_sa103s_view,
    generate_sa105_view,
    generate_sa110_view
)
from django.test import RequestFactory
import os
import django
from django.conf import settings
import json
import sys

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tax_project.settings")
django.setup()


def verify_endpoint(name, view_func, url):
    print(f"\nTesting {name} (GET)...")
    factory = RequestFactory()
    request = factory.get(url)

    response = view_func(request)

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
        verify_endpoint("SA103S", generate_sa103s_view,
                        '/api/generate/sa103s/')
        verify_endpoint("SA105", generate_sa105_view, '/api/generate/sa105/')
        verify_endpoint("SA110", generate_sa110_view, '/api/generate/sa110/')
    except Exception as e:
        print(f"Error during test: {e}")
