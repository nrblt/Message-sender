from rest_framework import status
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import UserAndChatId
from .serializers import UserAndChatIdSerializer

# Create your views here.

class UserAndChatViewSet(ModelViewSet):
    serializer_class=UserAndChatIdSerializer
    queryset=UserAndChatId.objects.all()

    def create(self, request):
        user = request.user

        if user.is_anonymous:
            raise NotAuthenticated("Not valid token")
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            is_existing = self.queryset.filter(tg_chat_id=serializer.data['tg_chat_id'])
            if is_existing:
                if is_existing.filter(user=user).exists():
                    raise PermissionDenied("You already registered")
                else:
                    raise PermissionDenied("This user is used by other telegram account")
            tg_and_user = UserAndChatId(user=user, tg_chat_id=serializer.data['tg_chat_id'])
            tg_and_user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
