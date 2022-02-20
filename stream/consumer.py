import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer


class BroadcastingConsumer(AsyncWebsocketConsumer):


    '''
        Any consumer based on Channels’ SyncConsumer or AsyncConsumer will 
        automatically provide you a self.channel_layer and self.channel_name attribute, 
        which contains a pointer to the channel layer instance and the channel name that 
        will reach the consumer respectively. Any message sent to that channel name - or 
        to a group the channel name was added to - will be received by the consumer much 
        like an event from its connected client, and dispatched to a named method on the 
        consumer. The name of the method will be the type of the event with periods replaced 
        by underscores

    '''

    async def connect(self):
        await self.channel_layer.group_add('finance_stream', self.channel_name)
        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('finance_stream', self.channel_name)


    async def broadcast_finance(self, event):
        # print(event)
        text_message = event['rate']
        encoded_weight = str(text_message)
        await self.send(encoded_weight)