from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

# Create your views here.
def main(request):
    return render(request, "main.html")

def login(request):
    return render(request, "login/login.html")

def register(request):
    return render(request, "login/register.html")

def forgot_login(request):
    return render(request, "login/forgot_login.html")

class TaskList(ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = "task/task_detail.html"

