# WSchannels/routings.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("", consumers.QuizConsumer.as_asgi()),
]