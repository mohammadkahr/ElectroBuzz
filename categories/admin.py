from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']
    list_per_page = 10

