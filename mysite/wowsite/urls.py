from django.urls import path, include
from . import views

loginpatterns = [
    path("login/", views.login, name = "login"),
    path("register/", views.register, name = "register"),
    path("forgot_login/", views.forgot_login, name = "forgot_login"),
]

addpatterns = [
    path("class/", views.AddClass.as_view(), name = "addclass"),
    path("spec/", views.AddSpec.as_view(), name = "addspec"),
]

urlpatterns = [
    path('', views.main, name="main"),
    path('account/', include(loginpatterns), name='account'),
    path('add/', include(addpatterns), name='add'),
    # path('about/', views.about, name='about'),
    path('task/', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('class/', views.ClassList.as_view(), name='classes'),
    path('class/<slug:slug>/', views.ClassDetail.as_view(), name='class'),
    path('role/<slug:role_slug>/', views.SpecByRole.as_view(), name='role'),
    path('role/<slug:role_slug>/<slug:spec_slug>/', views.SpecByRoleDetail.as_view(), name='spec'),
    path('edit/<slug:spec_slug>/', views.UpdateSpec.as_view(), name = 'editspec')
]

