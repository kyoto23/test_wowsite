from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task, WowClass

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

def show_menu(request, id):
    return main(request)

def show_class(request, class_slug):
    post = get_object_or_404(WowClass, slug=class_slug)

    data = {
        'title': post.title,
        'post': post,
    }
    return render(request, "wowsite/classes/class_detail.html", data)

class ClassList(ListView):
    model = WowClass
    template_name = "wowsite/classes/class_list.html"
    context_object_name = 'classes'

class TaskList(ListView):
    model = Task
    template_name = "wowsite/task/task_list.html"
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = "wowsite/task/task_detail.html"

