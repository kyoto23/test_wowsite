import logging
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Specialization, Task, WowClass
from .services import spec_by_role, published_class
from .forms import AddClassForm, AddSpecForm

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

class AddSpec(CreateView):
    form_class = AddSpecForm
    template_name = 'wowsite/forms/add.html'

    def get_success_url(self):
        return self.object.get_absolute_url()
    
class AddClass(AddSpec):
    form_class = AddClassForm

class ClassByRole(ListView):
    template_name = 'wowsite/classes/specs_by_role.html'
    context_object_name = 'specs'

    def get_queryset(self):
        return spec_by_role(role_slug=self.kwargs['role_slug'])
    
class ClassByRoleDetail(DetailView):
    model = Specialization
    template_name = 'wowsite/classes/detail_by_role.html'
    context_object_name = 'spec'
    slug_url_kwarg = 'spec_slug'

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
    context_object_name = 'task'

