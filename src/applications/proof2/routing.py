# -*- coding: utf-8 -*-
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat2/(?P<room_name>\w+)/$', consumers.Chat2Consumer.as_asgi()),
]
