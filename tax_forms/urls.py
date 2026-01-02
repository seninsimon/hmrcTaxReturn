from django.urls import path
from . import views

app_name = 'tax_forms'

urlpatterns = [
    path('api/generate/sa100/', views.generate_sa100_view, name='generate_sa100'),
    path('api/generate/sa102/', views.generate_sa102_view, name='generate_sa102'),
    path('api/generate/sa103s/', views.generate_sa103s_view, name='generate_sa103s'),
    path('api/generate/sa105/', views.generate_sa105_view, name='generate_sa105'),
    path('api/generate/sa110/', views.generate_sa110_view, name='generate_sa110'),
]
