from django.contrib import admin
from django.urls import path, include
from django.conf import settings

admin.site.site_header = 'Electro Admin'
admin.site.index_title = 'Admin'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Electro.urls')),
    path('', include('products.urls')),
    path('', include('categories.urls')),
    path('accounts/', include('allauth.urls')),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns