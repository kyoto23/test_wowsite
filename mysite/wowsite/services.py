from django.shortcuts import get_object_or_404
from .models import WowClass, Specialization, Role

def spec_by_role(role_slug):
    role = get_object_or_404(Role, slug = role_slug)
    queryset = Specialization.objects.filter(role_id = role.pk)

    return queryset

def published_class(model):
    return model.published.all()