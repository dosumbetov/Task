from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<slug:slug>/', MenuItemDetailView.as_view(), name='menu_item'),
]