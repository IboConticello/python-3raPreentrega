from django.urls import path
from django.shortcuts import render
from .views import *




urlpatterns = [
    path ('', inicio, name='inicio'),
    path ('cliente/', ClienteForm, name='cliente'),
    path ('producto/', ProductoForm, name='producto'),
    path ('envio/', EnvioForm, name='envio'),
]