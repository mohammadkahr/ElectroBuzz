from django.core.validators import MinValueValidator
from django.db import models
from mptt.models import MPTTModel

from django.contrib.auth.models import User
from products.models import Product


class banner(models.Model):
    header = models.CharField(max_length=255)
    caption = models.CharField(max_length=1000)
    image = models.FileField(upload_to='Electro/static/myapp/img/new', blank=True, null=True)
    active = models.BooleanField(default=False)
    link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.header


class adviser(models.Model):
    header = models.CharField(max_length=255)
    caption = models.CharField(max_length=1000)
    image = models.FileField(upload_to='Electro/static/myapp/img/new', blank=True, null=True)
    active = models.BooleanField(default=False)
    link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.header


class adsWithDiscount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='')
    discount = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.product.name


class bestSellerProduct(models.Model):
    productName = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='')
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.productName


class topSellingProduct(models.Model):
    productName = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='')
    # discount = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.productName

