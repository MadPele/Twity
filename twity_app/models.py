from django.db import models
from django.contrib.auth.models import User


class Twit(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Post title'
    )
    content = models.TextField(
        max_length=140,
        verbose_name='Content')
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'

    class Meta():
        verbose_name = "Twit"
        verbose_name_plural = "Twits"


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL)
    content = models.TextField(
        max_length=60,
        verbose_name='Content')
    post = models.ForeignKey(
        Twit,
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.content[0:20]}'

    class Meta():
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Message(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='From',
        null=True,
        on_delete=models.SET_NULL)
    to_user = models.ForeignKey(
        User,
        null=True,
        related_name='To',
        on_delete=models.SET_NULL)
    content = models.TextField(verbose_name='Content')

    def __str__(self):
        return f'Message from {self.from_user}'

    class Meta():
        verbose_name = "Massage"
        verbose_name_plural = "Messages"




