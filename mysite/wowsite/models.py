from datetime import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class PublishedManager(models.Manager): # Менеджер модели
    def get_queryset(self):
        return super().get_queryset().filter(is_published=WowClass.Status.PUBLISHED)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']

class WowClass(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Чорновик"
        PUBLISHED = 1, "Published"

    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    roles = models.ManyToManyField("Role", related_name='roles')

    published = PublishedManager()
    objects = models.Manager()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

class Specialization(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, default='')
    slug = models.SlugField(max_length=30, unique=True, db_index=True)
    wow_class = models.ForeignKey("WowClass", on_delete=models.PROTECT, related_name='wow_class')
    role = models.ForeignKey("Role", on_delete=models.PROTECT,null=True, related_name='role')

    def __str__(self):
        return self.title

class Role(models.Model):
    title = models.CharField(max_length=10, db_index=True)
    slug = models.SlugField(max_length=10, unique=True, db_index=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("role", kwargs={"role_slug": self.slug})
    
