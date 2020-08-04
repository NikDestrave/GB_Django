from django.shortcuts import render
import json


def main(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


def catalog(request):
    with open("static/catalog.json", "r", encoding="utf-8") as read_file:
        data_catalog = json.load(read_file)
    context = {
        'title': 'Каталог',
        'json_catalog': data_catalog
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
        'title': 'Продукт №1'
    }
    return render(request, 'mainapp/catalog/product_1.html', context)


def product_2(request):
    context = {
        'title': 'Продукт №2'
    }
    return render(request, 'mainapp/catalog/product_2.html', context)


def product_3(request):
    context = {
        'title': 'Продукт №3'
    }
    return render(request, 'mainapp/catalog/product_3.html', context)
