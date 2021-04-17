"""
ASGI config for SimpleCRM project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from SimpleCRM.settings import get_settings_module

os.environ.setdefault('DJANGO_SETTINGS_MODULE', get_settings_module())

application = get_asgi_application()
