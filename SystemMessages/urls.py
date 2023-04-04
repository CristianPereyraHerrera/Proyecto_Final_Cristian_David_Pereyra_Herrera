from django.urls import path
from SystemMessages.views import send_message, see_message, delete_message


urlpatterns = [
    path('messages/', see_message, name='SeeMessage'),
    path('messages/send_message/', send_message, name='SendMessage'),
    path('messages/send-message/<str:user_username>/', send_message, name='ReSendMessage'),
    path('messages/delete/<int:message_id>/', delete_message, name='DeleteMessage')
]
