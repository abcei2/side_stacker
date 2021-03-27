# app/chat/routing.py
from django.urls import re_path

from game.views import GameSideStacker

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', GameSideStacker.as_asgi() ),
]