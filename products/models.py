from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db import models
from categories.models import Category


class AdditionalInfo(models.Model):
    description = models.CharField(max_length=2000, blank=True, null=True)
    brand = models.CharField(max_length=255)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    screen_size = models.DecimalField(max_digits=5, decimal_places=2)
    model = models.CharField(max_length=255)
    ram = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    description = models.TextField()
    view_count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.FileField(upload_to='product/statics/img', blank=True, null=True)
    video = models.FileField(upload_to='product/statics/vid', null=True, blank=True)
    additionalInform = models.OneToOneField(AdditionalInfo, related_name='product', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', 'rating')

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='product/statics/rev/', null=True, blank=True)
    rating = models.PositiveIntegerField()
    # subject = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name


class PriceChange(models.Model):
    product = models.ForeignKey(Product, related_name='price_changes', on_delete=models.CASCADE)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    change_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

    class Meta:
        ordering = ('product', 'change_date')
