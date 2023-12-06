from django.contrib import admin
from app.models import *

admin.site.register(Menu)

class MenuTitleAdmin(admin.ModelAdmin):
    list_display = ('menu', 'name', 'created_at')
    search_fields = ('menu', 'name')
    list_filter = ('created_at',)

admin.site.register(MenuTitle, MenuTitleAdmin)

admin.site.register(MenuItem)
