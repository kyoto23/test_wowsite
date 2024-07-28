from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse 

# def login_user(request):
#     return render(request, "users/auth/login.html")

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/auth/login.html'

def logout_user(request):
    pass

def register(request):
    return render(request, "users/auth/register.html")

def forgot_login(request):
    return render(request, "users/auth/forgot_login.html")