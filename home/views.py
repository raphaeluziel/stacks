from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task
from .forms import Taskform


def home(request):

    return render(request, 'home/home.html')
  

def PostCreate(request):
    print(request.POST)
    x = request.POST.get('b1')
    print(x)
    if request.method == 'POST':
        form = Taskform(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('file')
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
    else:
        form = Taskform()
    return render(request, 'home/post_form.html', {'form': form})

def choose_type(request):
    return render(request, 'home/choose_type.html')