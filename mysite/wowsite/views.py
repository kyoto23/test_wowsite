import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .utils import DataMixin, SpecMixin
from .models import Specialization, Task, WowClass
from .services import spec_by_role, published_class
from .forms import AddClassForm, AddSpecForm

logger = logging.getLogger('main')

def main(request):
    logger.info("Old Logger Message")
    return render(request, "wowsite/main.html")
    
class AddSpec(SpecMixin, LoginRequiredMixin, CreateView):
    form_class = AddSpecForm

class UpdateSpec(SpecMixin, LoginRequiredMixin, UpdateView):
    model = Specialization
    fields = ['title', 'description', 'wow_class', 'role']
    slug_url_kwarg = 'spec_slug'

class SpecByRole(DataMixin, ListView):
    template_name = 'wowsite/classes/specs_by_role.html'
    context_object_name = 'specs'
    slug_url_kwarg = 'role_slug'

    def get_queryset(self):
        return spec_by_role(role_slug=self.kwargs['role_slug'])
    
class SpecByRoleDetail(DetailView):
    model = Specialization
    template_name = 'wowsite/classes/detail_by_role.html'
    context_object_name = 'spec'
    slug_url_kwarg = 'spec_slug'

class AddClass(AddSpec):
    form_class = AddClassForm

class ClassList(DataMixin, ListView):
    model = WowClass
    template_name = "wowsite/classes/class_list.html"
    context_object_name = 'classes'
    paginate_by = 5

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

