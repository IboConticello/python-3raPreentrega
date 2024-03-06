from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_app/', include('mi_app.urls')),
    path('', include('mi_app.urls')),
]
