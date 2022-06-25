from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from articles.models import (
    Categories,
    Articles
)


def split_list(lst, sz):
    return [lst[i::sz] for i in range(sz)]


def index(request):
    all_categories = Categories.objects.all().filter(is_published=True).order_by('-priority', 'name')
    args = {
        'active_menu': 'categories',
        'categories': split_list(all_categories, 2)
    }
    return render(request, 'categories/index.html', args)


def view(request, category_slug: str):
    try:
        category = Categories.objects.get(slug=category_slug)
    except ObjectDoesNotExist:
        return redirect('categories_index')

    all_articles = Articles.objects.all().filter(category_id=category.id).order_by('time_create')
    args = {
        'category': category,
        'articles': split_list(all_articles, 2)
    }
    return render(request, 'categories/view.html', args)
