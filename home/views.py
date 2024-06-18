from django.shortcuts import render, redirect

from .models import Message

def home(request):

    return render(request, 'home/home.html', {'messages': Message.objects.all()})
