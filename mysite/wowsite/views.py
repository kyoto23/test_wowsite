import logging
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .utils import DataMixin
from .models import Specialization, Task, WowClass
from .services import spec_by_role, published_class
from .forms import AddClassForm, AddSpecForm

logger = logging.getLogger('main')

# Create your views here.
def main(request):
    logger.info("Old Logger Message")
    return render(request, "wowsite/main.html")
    
class AddSpec(CreateView):
    form_class = AddSpecForm
    template_name = 'wowsite/forms/add.html'

    def get_success_url(self):
        return self.object.get_absolute_url()
    
class AddClass(AddSpec):
    form_class = AddClassForm

class UpdateSpec(UpdateView):
    model = Specialization
    fields = ['title', 'description', 'wow_class', 'role']
    template_name = 'wowsite/forms/add.html'
    slug_url_kwarg = 'spec_slug'

    def get_success_url(self):
        return self.object.get_absolute_url()

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

