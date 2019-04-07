from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Twit, Comment, Message


class Main(View):
    def get(self, request):
        twits = Twit.objects.all()
        comments = Comment.objects.all()
        return render(request, 'main.html', {'twits': twits, 'comments': comments})


class Login(View):
    pass


class Register(View):
    pass
