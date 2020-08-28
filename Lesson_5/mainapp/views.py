from django.shortcuts import render, get_object_or_404
import json

from basketapp.models import Basket
from mainapp.models import Product, CatalogCategory


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = CatalogCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(CatalogCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/catalog.html', content)

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }

    return render(request, 'mainapp/catalog.html', content)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contacts.html', context)


def games(request):
    context = {
        'title': 'Игры'
    }
    return render(request, 'mainapp/games.html', context)


def product_1(request):
    context = {
        'title': 'Schecter Demon-7'
    }
    return render(request, 'mainapp/catalog/product_1.html', context)


def product_2(request):
    context = {
        'title': 'Schecter OMEN-8'
    }
    return render(request, 'mainapp/catalog/product_2.html', context)


def product_3(request):
    context = {
        'title': 'Schecter C-5 BASS SGR'
    }
    return render(request, 'mainapp/catalog/product_3.html', context)
