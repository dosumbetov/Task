from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Menu(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MenuTitle(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.name

class MenuItem(models.Model):
    menu_title = models.ForeignKey(MenuTitle, on_delete=models.CASCADE)
    text = RichTextField()

    def __str__(self):
         return self.menu_title.name



@receiver(pre_save, sender=MenuTitle)
def slugify_name(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.name)
