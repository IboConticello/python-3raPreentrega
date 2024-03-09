from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_app/', include('mi_app.urls')),
    path('logout/', include('django.contrib.auth.urls')),
    path('', include('mi_app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
