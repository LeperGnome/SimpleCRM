from django.contrib import admin
from django.urls import path, include

from SimpleCRM.settings.base import VER

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/v{VER}/', include('core.urls'))
]
