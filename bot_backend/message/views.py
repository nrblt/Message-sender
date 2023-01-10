import telebot
from rest_framework import status
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from user.models import UserAndChatId

from .models import Message
from .serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    
    def create(self, request):
        user = request.user
        if user.is_anonymous:
            raise NotAuthenticated("Please authenticate")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            is_existing=UserAndChatId.objects.filter(user=user)
            text = serializer.data['text']
            if is_existing:
                formatted_text = user.first_name + ",я получил от тебя сообщение:\n" + text
                chat_id = is_existing[0].tg_chat_id
                send_message(chat_id,formatted_text)
            
            message = Message(user=user, text=text)
            message.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


API_TOKEN = '5761948695:AAEWDCLtbSbIaE-tZUBe0t_6SqSv6lis8go'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler()
def send_message(chat_id,text):
    bot.send_message(chat_id=chat_id,text=text)
