from django.urls import path
from django.shortcuts import render
from django import views
from .views import *
from . import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path ('', inicio, name='inicio'),
    path ('cliente/', cliente_form_view, name='cliente'),
    path ('producto/', producto_form_view, name='producto'),
    path ('envio/', envio_form_view, name='envio'),
    path ('busquedaCliente/', busqueda_cliente_view, name='busquedaCliente'),
    path ('buscar/', buscar, name='buscar'),
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
]