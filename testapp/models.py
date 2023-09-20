from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User

from bboard.models import Rubric, get_timestamp_path


class AdvUser(models.Model):
    is_activated = models.BooleanField(
        default=True,
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )


class Spare(models.Model):
    name = models.CharField(max_length=30)


class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare, through='Kit',
                                    through_fields=('machine', 'spare'))
    notes = GenericRelation('Note')


class Kit(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.IntegerField()


class SMS(models.Model):
    comment = models.CharField(max_length=120)

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sender"
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="receiver"
    )


class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type',
                                       fk_field='object_id')

    class Meta:
        permissions = (
            ('hide_comments', 'Можно скрывать заметки'),
        )


# Прямое наследование
# ##
# class Message(models.Model):
#     content = models.TextField()


# class PrivateMessage(Message):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.OneToOneField(Message, on_delete=models.CASCADE,
#                                    parent_link=True)


# Абстрактные модели
# ##
class Message(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        abstract = True
        ordering = ['name']


class PrivateMessage(Message):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = None

    class Meta(Message.Meta):
        pass


# Прокси-модели
class RevRubric(Rubric):
    class Meta:
        proxy = True
        ordering = ['-name']


class Img(models.Model):
    img = models.ImageField(
        verbose_name='Изображение',
        upload_to=get_timestamp_path,
        validators=[FileExtensionValidator(allowed_extensions=('jpg', 'png', 'gif'))]
    )

    desc = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
