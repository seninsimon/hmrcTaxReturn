"""
Django URLs Example for HMRC Tax Return Generators
Copy this to your Django app's urls.py
"""

from django.urls import path
from . import views

app_name = 'tax_returns'

urlpatterns = [
    # Separate endpoints for each form type
    path('api/generate/sa100/', views.generate_sa100_view, name='generate_sa100'),
    path('api/generate/sa102/', views.generate_sa102_view, name='generate_sa102'),

    # Alternative: Single endpoint with form_type parameter
    # path('api/generate/<str:form_type>/', views.generate_tax_form_view, name='generate_form'),
]
