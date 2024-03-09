from django.contrib import admin
from django.urls import path
from django import views
from .views import *
from . import views




urlpatterns = [
    path ('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', views.signout, name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('librosCreacion/', LibrosCreacion.as_view(), name='nuevo'),

    path('listaRomance/', RomanceLista.as_view(), name='romances'),
    path('romanceDetalle/<int:pk>/', RomanceDetalle.as_view(), name='romance'),
    path('romanceEdicion/<int:pk>/', RomanceUpdate.as_view(), name='romance_editar'),
    path('romanceBorrado/<int:pk>/', RomanceDelete.as_view(), name='romance_eliminar'),
    path('romanceDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('listaFantasia/', FantasiaLista.as_view(), name='fantasias'),
    path('fantasiaDetalle/<int:pk>/', FantasiaDetalle.as_view(), name='fantasia'),
    path('fantasiaEdicion/<int:pk>/', FantasiaUpdate.as_view(), name='fantasia_editar'),
    path('fantasiaBorrado/<int:pk>/', FantasiaDelete.as_view(), name='fantasia_eliminar'),
    path('fantasiaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]