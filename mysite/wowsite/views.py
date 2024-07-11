import logging
from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task, WowClass
from .services import spec_by_role, published_class

logger = logging.getLogger('main')

# Create your views here.
def main(request):
    logger.info("Old Logger Message")
    return render(request, "wowsite/main.html")

def login(request):
    return render(request, "wowsite/login/login.html")

def register(request):
    return render(request, "wowsite/login/register.html")

def forgot_login(request):
    return render(request, "wowsite/login/forgot_login.html")

def show_roles(request, role_slug):
    queryset = spec_by_role(role_slug)
    data = {'posts': queryset}

    return render(request, 'wowsite/classes/index.html', context=data)

def addspec(request):
    return render(request, 'wowsite/specialization/addspec.html')

class ClassList(ListView):
    model = WowClass
    template_name = "wowsite/classes/class_list.html"
    context_object_name = 'classes'

    def get_queryset(self):
        return published_class(self.model)
    
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

