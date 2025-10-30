import os
from django.core.wsgi import get_wsgi_application

# Point to the canonical settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'users_api.settings')

application = get_wsgi_application()
