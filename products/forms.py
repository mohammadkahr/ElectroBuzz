# products/forms.py
from django import forms
from .models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'rating', 'price', 'color', 'description', 'category', 'image', 'video']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'image', 'rating', 'subject', 'comment']
