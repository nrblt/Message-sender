from rest_framework import serializers

from .models import UserAndChatId


class UserAndChatIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAndChatId
        fields = ['tg_chat_id']
