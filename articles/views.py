from django.shortcuts import render


def index(request):
    args = {'active_menu': 'home'}
    return render(request, 'home.html', args)


def categories(request):
    args = {'active_menu': 'categories'}
    return render(request, 'categories.html', args)


def test(request):
    args = {'active_menu': 'test'}
    return render(request, 'test.html', args)
