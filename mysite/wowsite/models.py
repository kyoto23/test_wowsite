from datetime import datetime
from django.db import models
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

    published = PublishedManager()
    objects = models.Manager()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]