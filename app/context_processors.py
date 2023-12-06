from django.shortcuts import get_object_or_404
from .models import *


def menus(request):
    menu_list = Menu.objects.all().order_by('-created_at')
    menu_title_list = MenuTitle.objects.select_related('menu').order_by('-created_at')
    return {'menu_list': menu_list, 'menu_title_list': menu_title_list}