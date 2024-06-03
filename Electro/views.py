from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'myapp/home_page.html')

def detail_page(request):
    return render(request, 'myapp/productdetail.html')