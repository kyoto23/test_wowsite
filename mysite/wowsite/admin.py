from django.contrib import admin, messages
from .models import Task, WowClass, Role, Specialization

@admin.register(WowClass)
class WowClassAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'description', 'roles', 'tags', 'is_published']
    # filter_horizontal = ['roles']
    list_display = ('title', 'created', 'is_published', 'brief_info')
    list_display_links = ('title', )
    list_editable = ('is_published', )
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'tags__name']
    list_filter = ['roles__title', 'is_published']
    readonly_fields = ['slug']

    @admin.display(description="Довжина опису", ordering='description')
    def brief_info(self, wowclass: WowClass):
        return f"Опис {len(wowclass.description)} символів."
    
    @admin.display(description="Задати статус - PUBLISHED")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=WowClass.Status.PUBLISHED)
        self.message_user(request, f"Змінено {count} записа/-ів")

    @admin.display(description="Задати статус - DRAFT")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=WowClass.Status.DRAFT)
        self.message_user(request, f"Знято з публікації {count} записа/-ів", messages.WARNING)

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