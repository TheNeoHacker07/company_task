from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.crypto import get_random_string
from django.contrib.auth.base_user import BaseUserManager

#Обьявляем класс менеджер для создания пользавателя, и в ней определяем три функции,

class UserManager(BaseUserManager):

    #делаем так чтобы регистрация шла только по имейлу
    def _create_user(self, email, password, **extra):
        if not email:
            raise ValueError('Email-поле обязательное')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email, password, **extra):
        user = self._create_user(email, password, **extra)
        user.create_activation_code()  #функция для создания активационного кода в класс User
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra):
        extra.setdefault('is_active', True)
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        user=self._create_user(email, password, **extra)
        return user
    


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=10, blank=False)
    second_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=10, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def create_activation_code(self):
        code = get_random_string(length=10, allowed_chars='0123456789')
        self.activation_code = code
        