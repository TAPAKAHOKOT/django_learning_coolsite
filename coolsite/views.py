from django.shortcuts import render


def home_view(request):
    args = {'active_menu': 'home'}
    return render(request, 'home.html', args)


def test_view(request):
    args = {'active_menu': 'test'}
    return render(request, 'test.html', args)
