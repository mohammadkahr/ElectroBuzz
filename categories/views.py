from django.shortcuts import render
from categories.models import Category
import random


# Create your views here.
def shopByCategory(request):
    categories = list(Category.objects.all())
    random_categories = random.sample(categories, min(len(categories), 6))
    context = {'categories': random_categories}
    return render(request, 'myapp/home_page.html', context)

