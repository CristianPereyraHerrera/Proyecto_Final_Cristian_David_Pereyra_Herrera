from django.urls import path
from SystemMessages.views import inbox, send_message, see_message

urlpatterns = [
    path('messages/', inbox, name='Messages'),
    path('messages/send_message/', send_message, name='SendMessage'),
    path('messages/see_message/', see_message, name='SeeMessage'),
]
