"""
WSGI config for confectionery project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv
from dj_static import MediaCling, Cling


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

load_dotenv()

application = Cling(MediaCling(get_wsgi_application()))
