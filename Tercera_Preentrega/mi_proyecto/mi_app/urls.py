from django.urls import path
from django.shortcuts import render
from .views import *




urlpatterns = [
    path ('', inicio, name='inicio'),
    path ('cliente/', cliente_form_view, name='cliente'),
    path ('producto/', producto_form_view, name='producto'),
    path ('envio/', envio_form_view, name='envio'),
    path ('busquedaCliente/', busqueda_cliente_view, name='busquedaCliente'),
    path ('buscar/', buscar, name='buscar'),
]