from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.banner)
class bannerAdmin(admin.ModelAdmin):
    list_display = ['header', 'caption', 'active', 'image', 'link']
    search_fields = ['header', 'active']
    list_editable = ['active', 'link']
    list_per_page = 10


@admin.register(models.adviser)
class adviserAdmin(admin.ModelAdmin):
    list_display = ['header', 'caption', 'active', 'image', 'link']
    search_fields = ['header', 'active']
    list_editable = ['active', 'link']
    list_per_page = 10



