# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here.

class SnippetModelViewSet(ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
