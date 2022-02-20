import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
import django
django.setup()

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from .routing import websocket_urlpatterns
from channels.routing import get_default_application


django_asgi_app = get_asgi_application()



application =  ProtocolTypeRouter ({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack (URLRouter(websocket_urlpatterns))
})