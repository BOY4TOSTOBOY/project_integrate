# -*- coding: utf-8 -*-
from django.urls import path, re_path

from . import consumers
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]


websocket_urlpatterns = [
    re_path(r'ws/chat2/(?P<room_name>\w+)/$', consumers.Chat2Consumer.as_asgi()),
]
