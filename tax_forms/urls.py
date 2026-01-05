from django.urls import path
from . import views

app_name = 'tax_forms'

urlpatterns = [
    path('api/generate/unified/', views.generate_unified_pdf_view,
         name='generate_unified'),
]
