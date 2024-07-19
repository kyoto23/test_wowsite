from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify

# Create your models here.

class PublishedManager(models.Manager):
    '''Менеджер для перевірки, чи клас опублікований''' # Менеджер модели
    def get_queryset(self):
        return super().get_queryset().filter(is_published=WowClass.Status.PUBLISHED)

class Task(models.Model):
    '''Модель для тасок(ToDo)'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Користувач")
    title = models.CharField(max_length=100, verbose_name="Задача")
    description = models.TextField(null=True, blank=True, verbose_name="Опис")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Опис")
    complete = models.BooleanField(default=False, verbose_name="Виконано?")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']

class WowClass(models.Model):
    '''Модель для класів в WoW'''
    class Status(models.IntegerChoices):
        DRAFT = 0, "Чорновик"
        PUBLISHED = 1, "Published"

    title = models.CharField(max_length=30, verbose_name='Назва класу')
    slug = models.SlugField(unique=True, db_index=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Опис")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), 
                                       default=Status.DRAFT, verbose_name="Статус")
    roles = models.ManyToManyField("Role", related_name='roles', verbose_name="Ролі")
    tags = TaggableManager(verbose_name="Теги")    

    objects = models.Manager()
    published = PublishedManager()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("class", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.lower())
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Класси"
        verbose_name_plural = "Класси"
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

class Specialization(models.Model):
    '''Модель для спеків'''
    title = models.CharField(max_length=30, verbose_name="Назва спеку")
    description = models.TextField(blank=True, default='', verbose_name="Опис")
    slug = models.SlugField(max_length=30, unique=True, db_index=True)
    wow_class = models.ForeignKey("WowClass", on_delete=models.PROTECT, related_name='wow_class', verbose_name="Класс")
    role = models.ForeignKey("Role", on_delete=models.PROTECT,null=True, related_name='role', verbose_name="Роль")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("spec", kwargs={"role_slug":self.role.slug, "spec_slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.lower())
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Спеціалізації"
        verbose_name_plural = "Спеціалізації"
        ordering = ['wow_class']

class Role(models.Model):
    '''Модель для ролей в WoW'''
    title = models.CharField(max_length=10, db_index=True, verbose_name="Назва ролі")
    slug = models.SlugField(max_length=10, unique=True, db_index=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("role", kwargs={"role_slug": self.slug})
    
    class Meta:
        verbose_name = "Ролі"
        verbose_name_plural = "Ролі"
        indexes = [
            models.Index(fields=['slug'])
        ]
        ordering = ['pk']
    
class Menu(models.Model):
    '''Модель для хедер пунктів'''
    title = models.CharField(max_length=20, db_index=True, verbose_name="Назва пункту")
    slug = models.SlugField(max_length=10, unique=True, db_index=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Пункти меню"
        verbose_name_plural = "Пункти меню"
        ordering = ['pk']