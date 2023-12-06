from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import *


class HomePageView(TemplateView):
    template_name = 'main/index.html'




class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'pages/menu_item.html'
    context_object_name = 'menu_item'

    def get_object(self, queryset=None):
        return get_object_or_404(MenuItem, menu_title__slug=self.kwargs['slug'])
