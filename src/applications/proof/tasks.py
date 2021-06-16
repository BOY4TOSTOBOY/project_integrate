# -*- coding: utf-8 -*-
from asgiref.sync import async_to_sync
from celery import shared_task  # TODO: Есть вариации использования как ниже
from system.celery_app import app as celery_app
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()


@shared_task
def sum(channel_name, x: int, y: int):
    """
    Задача выполняемая с помощью celery worker и реализующая сложение двух чисел.
    После выполнения отправляет значение в канал websocket.

    :param channel_name: имя websocket канала
    :type channel_name: без понятия =)

    :param x: Первое число
    :type x: int

    :param y: Второе число
    :type y: int

    :return: Нет возвращаемого значения
    :rtype: None
    """
    message = '{}+{}={}'.format(x, y, int(x) + int(y))
    async_to_sync(channel_layer.send)(channel_name, {"type": "chat.message", "message": message})


@celery_app.task
def mul(channel_name, x: int, y: int):
    """
    Задача выполняемая с помощью celery worker и реализующая умножение двух чисел.
    После выполнения отправляет значение в канал websocket.

    :param channel_name: имя websocket канала
    :type channel_name: без понятия =)

    :param x: Первое число
    :type x: int

    :param y: Второе число
    :type y: int

    :return: Нет возвращаемого значения
    :rtype: None
    """
    message = '{}+{}={}'.format(x, y, int(x) * int(y))
    async_to_sync(channel_layer.send)(channel_name, {"type": "chat.message", "message": message})
