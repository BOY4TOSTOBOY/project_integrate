# -*- coding: utf-8 -*-
from django.test import TestCase
from .models import Snippet
# Create your tests here.


class SnippetsTest(TestCase):
    fixtures = ['initial_data']  # loads fixture

    def test_loaded_fixtures(self):
        queryset = Snippet.objects.all()
        self.assertEqual(queryset.count(), 2)
