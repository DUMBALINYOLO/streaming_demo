from __future__ import unicode_literals, absolute_import
from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from stream.models import FinanceLog
import random


channel_layer = get_channel_layer()


def get_finance_data():

    '''
        Lets assume this scripts is getting data from the api
    '''

    symbols = ["USD", "EUR", 'ETHEUR', 'ETHUSD']

    data = {}

    data['currency'] = random.choice(symbols)
    data['rate'] = random.randint(1000, 1000000)

    return data




@shared_task
def stream_finance():

    '''
        Bridge between your channels, the worker and the finance api

        The channel layer is for high-level application-to-application communication. 
        When you send a message, it is received by the consumers listening to the group 
        or channel on the other end. What this means is that you should send high-level 
        events over the channel layer, and then have consumers handle those events, 
        and do appropriate low-level networking to their attached client.

        Using Outside Of Consumers
        You’ll often want to send to the channel layer from outside of the scope of a consumer, 
        and so you won’t have self.channel_layer.
        In this case, you should use the get_channel_layer function to retrieve it:

        Then, once you have it, you can just call methods on it. Remember 
        that channel layers only support async methods, 
        so you can either call it from your own asynchronous context:


    '''


    finance_data = get_finance_data()

    async_to_sync(channel_layer.group_send)(
                                    'finance_stream', {
                                    'type': 'broadcast_finance',
                                    'rate': finance_data['rate']
                                }
                            )
    try:
        FinanceLog.objects.create(
                    rate = finance_data['rate'],
                    currency = finance_data['currency'],
                )
    except:
        print('Something is wrong with your worker')

