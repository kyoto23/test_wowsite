from django.urls import path, include
from . import views

loginpatterns = [
    path("login/", views.login, name = "login"),
    path("register/", views.register, name = "register"),
    path("forgot_login/", views.forgot_login, name = "forgot_login"),
]

urlpatterns = [
    path('', views.main, name="main"),
    path('account/', include(loginpatterns), name='account'),
    path('task/', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('menu/<int:id>', views.show_menu, name='menu'),
    path('class/', views.ClassList.as_view(), name='classes'),
    path('class/<slug:class_slug>/', views.show_class, name='class'),
]


