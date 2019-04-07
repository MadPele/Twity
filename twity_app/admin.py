from django.contrib import admin
from .models import Twit, Comment, Message


@admin.register(Twit)
class TwitAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
