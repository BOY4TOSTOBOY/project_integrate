from django.urls import path
from . import views
from .views import ProcessHookView

app_name = 'integrate'
urlpatterns = [
    path('', views.index, name='portal'),
    path('results/', views.results, name='results'),
    path('hook/', ProcessHookView.as_view(), name='hook')
]
