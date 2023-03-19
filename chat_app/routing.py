from django.urls import re_path

from . import consumers

websocket_urpatterns = [
    re_path(r'ws/chat_app/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer)
]