from django.urls import path
from . import views
from .views import HookView

app_name = 'integrate'
urlpatterns = [
    path('', views.index, name='portal'),
    path('results/', views.results, name='results'),
    path('hook/', HookView.as_view(), name='hook')
]
