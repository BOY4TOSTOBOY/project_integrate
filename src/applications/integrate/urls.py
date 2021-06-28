from django.urls import path
from . import views

app_name = 'integrate'
urlpatterns = [
    path('', views.index, name='portal'),
    path('results/', views.results, name='results')
]
