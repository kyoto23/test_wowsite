from django import template
from wowsite.models import Role
import wowsite.views as views

register = template.Library()

@register.simple_tag()
def get_menu():
    return views.menu

@register.inclusion_tag("wowsite/base_and_tags/navigation.html")
def navigation():
    menu = views.menu
    return {'menu':menu}

@register.inclusion_tag('wowsite/classes/class_roles.html')
def show_roles():
    roles = Role.objects.all()
    return {'roles': roles}
