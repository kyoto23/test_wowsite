from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name = "login"),
    path("logout/", views.logout_user, name = "logout"),
    path("register/", views.register, name = "register"),
    path("forgot_login/", views.forgot_login, name = "forgot_login"),
]
