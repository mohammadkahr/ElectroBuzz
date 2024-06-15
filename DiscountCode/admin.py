from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent',
                    'discount_amount', 'max_discount',
                    'active')
    list_editable = ('discount_percent', 'discount_amount',
                     'max_discount',
                     'active')
    list_per_page = 10
    search_fields = ['code', 'discount_percent', 'discount_amount',
                     'max_discount', 'applicable_products', 'valid_to',
                     'active']
