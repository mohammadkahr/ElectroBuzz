from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
    search_fields = ['user__istartswith']
    list_per_page = 10


@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']
    list_per_page = 10
