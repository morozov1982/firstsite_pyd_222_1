from django.contrib.auth.models import AbstractUser
from django.db import models


class BbUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatars',
        blank=True,
        verbose_name='Аватарка',
    )

    age = models.PositiveIntegerField(
        verbose_name='Возраст',
        blank=True,
        null=True,
    )
