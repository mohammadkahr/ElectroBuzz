from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'rating', 'view_count', 'image']
    list_editable = ['price', 'rating', 'view_count']
    list_per_page = 10
    search_fields = ['name__istartswith']


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'rating', 'active']
    list_editable = ['rating', 'active']
    list_per_page = 10
    search_fields = ['product__istartswith']


@admin.register(models.PriceChange)
class PriceChange(admin.ModelAdmin):
    list_display = ['product', 'old_price', 'new_price']
    list_editable = ['old_price', 'new_price']
    list_per_page = 10
    search_fields = ['product__istartswith']

@admin.register(models.AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ['product', 'brand', 'model']
    list_editable = ['model']
    list_per_page = 10
    search_fields = ['product__istartswith']

