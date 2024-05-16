from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

menu = [{'title': 'Головна', 'url_name' : 'main'},
        {'title': 'Вхід', 'url_name' : 'login'},
        {'title': 'Реєстрація', 'url_name' : 'register'},
        ]

# Create your views here.
def main(request):
    data = {'menu' : menu}
    return render(request, "base.html", context=data)

def login(request):
    return render(request, "wowsite/login/login.html")

def register(request):
    return render(request, "wowsite/login/register.html")

def forgot_login(request):
    return render(request, "wowsite/login/forgot_login.html")

class TaskList(ListView):
    model = Task
    template_name = "wowsite/task/task_list.html"
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = "wowsite/task/task_detail.html"

