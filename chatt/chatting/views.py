from chatt.settings import CHANNEL_LAYERS
from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json, time

# Create your views here.
# def index(request):
#     return render(request, 'chat/index.html')

# def room(request):
#     return render(request, 'chat/room.html')

async def home(request):
    for i in range(1, 10):
        channel_layer = get_channel_layer()
        data = {'count': i}
        await (channel_layer.group_send)(
            'new_consumer_group', {
                'type': 'send_notification',
                'value': json.dumps(data)
            }
        )
        time.sleep(1)
        
        return render(request, 'chat/home.html')