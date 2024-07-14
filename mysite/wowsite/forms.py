from django.forms import ModelForm
from .models import WowClass, Specialization

class AddClassForm(ModelForm):
    class Meta:
        model = WowClass
        fields = ['title', 'description','roles', 'is_published', 'tags']

class AddSpecForm(ModelForm):
    class Meta:
        model = Specialization
        fields = ['title', 'description', 'wow_class', 'role']
