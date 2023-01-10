from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

# Create your models here.
User = get_user_model()

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    created = models.DateTimeField(default=timezone.now)
