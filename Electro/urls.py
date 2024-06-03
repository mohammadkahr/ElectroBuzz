from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_page, name='home_page'),
    path('detail', views.detail_page, name='detail_page'),
]