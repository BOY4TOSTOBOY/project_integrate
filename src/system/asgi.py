# -*- coding: utf-8 -*-
"""
ASGI config for system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from typing import List

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'system.settings')
django_asgi_application = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from applications.proof import urls as proof_urls
from applications.proof2 import urls as proof2_urls


def websocket_urlpatterns(urlpatterns: List[list]) -> list:
    """ websocket_urlpatterns([[re_path('1', ...), ...], [re_path('2', ...)]]) ->
    [re_path('1', ...), re_path('2', ...), ...]

    Функция возвращает объединеный список всех веб-сокет урлов,
    которые зарегестрированны в системе.
    Получает список всех 'websocket_urlpatters' из каждого приложения
    и возвращает общий список.

    """
    ws_urls = []
    for urlpattern in urlpatterns:
        ws_urls.extend(urlpattern)
    return ws_urls


application = ProtocolTypeRouter({
    'http': django_asgi_application,
    # Just HTTP for now. (We can add other protocols later.)
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns([
            proof_urls.websocket_urlpatterns,
            proof2_urls.websocket_urlpatterns,
        ]))
    ),
})
