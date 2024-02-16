from django.contrib import admin
from django.urls import path, include
from mi_aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('formulario/', include('mi_aplicacion.urls')),
]
