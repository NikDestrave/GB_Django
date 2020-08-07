from django.shortcuts import render
import json

from mainapp.models import Product


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    products = Product.objects.all()
    context = {
        'title': 'Каталог',
        'products': products
    }
    return render(request, 'mainapp/catalog.html', context)


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
