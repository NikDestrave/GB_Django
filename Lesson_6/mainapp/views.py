import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, CatalogCategory


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def main(request):
    basket = get_basket(request.user)
    content = {
        'title': 'Главная',
        'basket': basket
    }
    return render(request, 'mainapp/index.html', content)


def catalog(request, pk=None):

    title = 'товары'
    links_menu = CatalogCategory.objects.all()

    basket = get_basket(request.user)

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

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': basket
    }

    return render(request, 'mainapp/catalog.html', content)


def contacts(request):
    basket = get_basket(request.user)
    content = {
        'title': 'Контакты',
        'basket': basket
    }
    return render(request, 'mainapp/contacts.html', content)


def games(request):
    basket = get_basket(request.user)
    content = {
        'title': 'Игры',
        'basket': basket
    }
    return render(request, 'mainapp/games.html', content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': CatalogCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


def product_1(request):
    basket = get_basket(request.user)
    content = {
        'title': 'Schecter Demon-7',
        'basket': basket
    }
    return render(request, 'mainapp/catalog/product_1.html', content)


def product_2(request):
    basket = get_basket(request.user)
    context = {
        'title': 'Schecter OMEN-8',
        'basket': basket
    }
    return render(request, 'mainapp/catalog/product_2.html', context)


def product_3(request):
    basket = get_basket(request.user)
    context = {
        'title': 'Schecter C-5 BASS SGR',
        'basket': basket
    }
    return render(request, 'mainapp/catalog/product_3.html', context)
