from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('product/<int:product_id>/', views.detail_page, name='detail_page'),
    path('404', views.page_not_found, name='page_not_found'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)