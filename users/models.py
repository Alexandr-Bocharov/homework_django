from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


NULLABLE = {'null': True,
            'blank': True}

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='avatars/', verbose_name='фото', **NULLABLE)
    phone_number = PhoneNumberField(verbose_name='номер телефона', **NULLABLE)
    # phone_number = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(verbose_name='страна', max_length=100, **NULLABLE)

    token = models.CharField(max_length=100, verbose_name='token', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email

