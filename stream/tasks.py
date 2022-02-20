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

