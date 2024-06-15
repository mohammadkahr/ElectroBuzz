import random
from django.shortcuts import get_object_or_404
from Electro.models import banner, adviser
from categories.models import Category
from products.models import Product
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomLoginForm, CustomSignupForm

logger = logging.getLogger(__name__)


# Create your views here.
def home_page(request):
    categories = list(Category.objects.all())
    random_categories = random.sample(categories, min(len(categories), 6))

    active_banners = banner.objects.filter(active=True).first()

    active_advisers = adviser.objects.filter(active=True).first()

    products = list(Product.objects.all())
    random_p = random.sample(products, min(len(products), 7))
    first_products = random_p[0]
    random_products = random_p[1:7]

    top_products = Product.objects.order_by('-view_count')[:7]
    first_product_v = top_products[0]
    next_six_products_v = top_products[1:7]

    context = {
        'categories': random_categories,
        'active_banner': active_banners,
        'active_adviser': active_advisers,
        'first_products': first_products,
        'products': random_products,
        'first_product_v': first_product_v,
        'next_six_products_v': next_six_products_v
    }

    return render(request, 'myapp/home_page.html', context)


def get_reviews_for_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
        reviews = product.reviews.filter(active=True)
        return reviews
    except Product.DoesNotExist:
        return None


def get_related_products(product, num_related=4):
    return Product.objects.filter(category=product.category).exclude(id=product.id)[:num_related]


def detail_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    reviews = get_reviews_for_product(product_id)

    related_products = get_related_products(product)

    context = {
        'product': product,
        'reviews': reviews,
        'related_products': related_products
    }
    return render(request, 'myapp/productdetail.html', context)


def page_not_found(request):
    return render(request, '404.html')


def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home_page')
    else:
        form = CustomSignupForm()
    return render(request, 'myapp/home_page.html', {'form': form})


def login_(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}. You are now logged in.")
                return redirect('home_page')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()
    return render(request, 'myapp/home_page.html', {'login_form': form})


