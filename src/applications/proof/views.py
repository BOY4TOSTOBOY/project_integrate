# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'proof/index.html', {})


def room(request, room_name):
    return render(request, 'proof/room.html', {
        'room_name': room_name
    })
