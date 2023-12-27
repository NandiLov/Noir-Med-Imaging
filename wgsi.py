"""
WSGI config for Noir-Med-Imaging project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""


import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the directory containing your Django project to the Python path
path = '/home/noirmed/Noir-Med-Imaging/'
if path not in sys.path:
    sys.path.insert(0, path)

# Set the environment variable for your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NoirMedImaging.settings")

# Initialize the WSGI application
application = get_wsgi_application()