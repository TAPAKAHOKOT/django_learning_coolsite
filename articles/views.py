from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from articles.models import Categories


split_list = lambda lst, sz: [lst[i::sz] for i in range(sz)]

def index(request):
    args = {'active_menu': 'home'}
    return render(request, 'home.html', args)


def categories(request):
    all_categories = Categories.objects.all().filter(is_published=True).order_by('-priority', 'id')
    args = {
        'active_menu': 'categories',
        'categories': split_list(all_categories, 2)
    }
    return render(request, 'categories.html', args)


def category_index(request, category_slug: str):
    try:
        category = Categories.objects.get(slug=category_slug)
    except ObjectDoesNotExist:
        return redirect('categories')

    args = {
        'category': category
    }
    return render(request, 'categories/index.html', args)


def test(request):
    args = {'active_menu': 'test'}
    return render(request, 'test.html', args)
