"""
ASGI config for chatt project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from chatting.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatt.settings')

application = get_asgi_application()

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     # Just HTTP for now. (We can add other protocols later.)
# })

ws_pattern = [
    path('ws/test/', TestConsumer.as_asgi()),
    path('ws/new/', NewConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_pattern)
})