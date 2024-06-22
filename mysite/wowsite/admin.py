from django.contrib import admin
from .models import Task, WowClass, Role, Specialization

@admin.register(WowClass)
class WowClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'is_published',)
    list_display_links = ('id', 'title')
    list_editable = ('is_published', )
    
@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'wow_class', 'role')
    list_display_links = ('title', )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user')
    list_display_links = ('title', )

# admin.site.register(WowClass, WowClassAdmin)
admin.site.register(Role)