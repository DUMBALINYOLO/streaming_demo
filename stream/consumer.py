import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer


class BroadcastingConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add('finance_stream', self.channel_name)
        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('finance_stream', self.channel_name)


    async def broadcast_finance(self, event):
        text_message = event['rate']
        encoded_weight = str(text_message)
        await self.send(encoded_weight)