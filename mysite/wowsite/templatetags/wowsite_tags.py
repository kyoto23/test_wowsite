from django import template
import wowsite.views as views

register = template.Library()

@register.simple_tag()
def get_menu():
    return views.menu

@register.inclusion_tag('wowsite/list_menu.html')
def show_menu():
    menu = views.menu
    return {'menu': menu}

@register.inclusion_tag("wowsite/classes/navigation.html")
def navigation():
    menu = views.menu
    return {'menu':menu}