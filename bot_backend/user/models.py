from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager

# Create your models here.
        
class CustomUserManager(UserManager):
    def _create_user(self, login, email, password, **extra_fields):

        if not login:
            raise ValueError("The given login must be set")
        email = self.normalize_email(email)
        user = self.model(login=login, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(login, email, password, **extra_fields)

    def create_superuser(self, login, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(login, email, password, **extra_fields)

class User(AbstractUser):
    login=models.CharField(max_length=200, blank=False, unique=True)
    username=models.CharField(max_length=200, blank=False)
    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["first_name"]
    objects = CustomUserManager()

class UserAndChatId(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tg_chat_id = models.IntegerField()
