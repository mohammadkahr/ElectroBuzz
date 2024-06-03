from django import forms
from .models import Product, ProductImage, ProductVideo, DiscountCode, Cart, CartItem, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductVideoForm(forms.ModelForm):
    class Meta:
        model = ProductVideo
        fields = ['video']

class DiscountCodeForm(forms.ModelForm):
    class Meta:
        model = DiscountCode
        fields = ['code', 'percentage', 'amount', 'max_discount',
                  'applicable_products', 'applicable_categories', 'start_date', 'end_date', 'active']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user']

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent', 'description']
