"""
ASGI config for food_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import os
import logging
from django.core.asgi import get_asgi_application

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_project.settings')

try:
    application = get_asgi_application()
except Exception as e:
    logger.error("Error loading ASGI application", exc_info=e)
    raise
