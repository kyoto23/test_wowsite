from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Role, Specialization, Task, WowClass
from .services import spec_by_role

menu = [{'id':1, 'title': 'Головна', 'url_name' : 'main'},
        {'id':2, 'title': 'Вхід', 'url_name' : 'login'},
        {'id':3, 'title': 'Реєстрація', 'url_name' : 'register'},
        ]

# Create your views here.
def main(request):
    return render(request, "wowsite/main.html")

def login(request):
    return render(request, "wowsite/login/login.html")

def register(request):
    return render(request, "wowsite/login/register.html")

def forgot_login(request):
    return render(request, "wowsite/login/forgot_login.html")

def show_roles(request, role_slug):
    queryset = spec_by_role(role_slug)

    data = {
        'posts': queryset,
    }
    return render(request, 'wowsite/classes/index.html', context=data)

class ClassList(ListView):
    model = WowClass
    template_name = "wowsite/classes/class_list.html"
    context_object_name = 'classes'

    def get_queryset(self):
        return WowClass.published.filter()
    
class ClassDetail(DetailView):
    model = WowClass
    template_name = "wowsite/classes/class_detail.html"
    context_object_name = 'class'

class TaskList(ListView):
    model = Task
    template_name = "wowsite/task/task_list.html"
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = "wowsite/task/task_detail.html"

