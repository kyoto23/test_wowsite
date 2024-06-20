from django.contrib import admin
from .models import Task, WowClass, Role, Specialization

# Register your models here.
admin.site.register(Task)
admin.site.register(WowClass)
admin.site.register(Role)
admin.site.register(Specialization)