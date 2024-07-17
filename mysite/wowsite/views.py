import logging
from typing import Any
from django.db.models.query import QuerySet
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task, WowClass
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

class ShowRoles(ListView):
    template_name = 'wowsite/classes/specs_by_role.html'
    context_object_name = 'specs'

    def get_queryset(self):
        return spec_by_role(role_slug=self.kwargs['role_slug'])

def add_class(request):
    if request.method == 'POST':
        form = AddClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
    else:
        form = AddClassForm()

    return render(request, 'wowsite/forms/add.html', context={'form': form})

class AddSpec(View):
    def get(self, request):
        form = AddSpecForm()
        data = {'form': form}
        return render(request, 'wowsite/forms/add.html', data)

    def post(self, request):
        form = AddSpecForm(request.POST)
        if form.is_valid():
            form.save()
            role = form.cleaned_data['role']
            return redirect(reverse("role", kwargs={"role_slug": role.slug}))
        
        data = {'form': form}
        return render(request, 'wowsite/forms/add.html', data)

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

