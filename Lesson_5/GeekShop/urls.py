"""GeekShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from GeekShop import settings
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('catalog/', include('mainapp.urls', namespace='catalog')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('contacts/', views.contacts, name='contacts'),
    path('games/', views.games, name='games'),
    path('catalog/product_1', views.product_1, name='product_1'),
    path('catalog/product_2', views.product_2, name='product_2'),
    path('catalog/product_3', views.product_3, name='product_3'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
