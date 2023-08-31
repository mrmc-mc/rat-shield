import json
import random
from django.utils.timezone import now
from django.db.models import Q
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class QuizConsumer(AsyncJsonWebsocketConsumer):
    
    async def connect(self):
        print("connected: ", self)
        await self.accept()

    async def disconnect(self, close_code):

        try:
            print("disconncted")
        except Exception as e:
            print("disconnect:error: ",e)

    async def receive(self, text_data):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        try:
            print("=============recieved===========")
            _data = json.loads(text_data)
            print(_data)
            print("-------------end rec---------------")
                
        except Exception as e:
            print(e)

    async def send_message(self, res):
        """Receive message from room group"""
        # Send message to channel
        try:
            await self.send_json(res["message"])
        except Exception as e:
            print("send_message: ", e)

