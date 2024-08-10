from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task
from .forms import Taskform


def home(request):

    return render(request, 'home/home.html')


class filterTask(View):

    def get(self, request):
        form = Taskform(request.GET.get('priorityChoice'))
        ans = Task.objects.all().values()
        return render(request, 'home/filter-task.html', context={'ans':ans});

    def post(self, request):

        

        print("HERE")
        
        form = Taskform()
        if request.method == 'GET':
            print("GET")
            form = Taskform(request.GET.get('priorityChoice'))
            ans = Task.objects.filter(priority = form).values()
        else:
            print("WHat")
             

        return redirect(request, 'home:home')
    

