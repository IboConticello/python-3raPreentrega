from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.formulario_insertar, name='formulario_insertar'),
    path('buscar/', views.buscar, name='buscar'),
    path('resultado/', views.resultado_busqueda, name='resultado_busqueda'),
]
