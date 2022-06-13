"""bot URL Configuration

created by ilunga ntita
"""
from django.urls import path
from .views import bot, messages

urlpatterns = [
    path('', bot, name="home"),
    path('messages/<id>', messages, name="messages"),
]
