from django.shortcuts import render

from mainapp.models import Test, TestCategory


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', context)


def catalogs(request):
    context = {
        'title': 'Тесты',
        'tests': Test.objects.all(),
        'catalog': TestCategory.objects.filter(),
    }
    return render(request, 'mainapp/tests.html', context)
