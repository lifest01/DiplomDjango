from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('output/', views.index, name = 'script'),
]