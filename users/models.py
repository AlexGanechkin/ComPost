from django.core.validators import EmailValidator
from django.db import models

from django.contrib.auth.models import AbstractUser

from compost.models import BaseModel


class User(AbstractUser, BaseModel):
    REQUIRED_FIELDS = []
    first_name = False
    last_name = False
    last_login = False
    date_joined = False

    birth_day = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
