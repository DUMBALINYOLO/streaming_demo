from channels.routing import ProtocolTypeRouter,URLRouter


from django.urls import path
from stream import consumer



websocket_urlpatterns=[
    path('ws/financeData/',consumer.BroadcastingConsumer.as_asgi()),
]