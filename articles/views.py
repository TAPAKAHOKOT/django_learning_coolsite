from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    CreateView
)
from articles.models import (
    Categories,
    Articles
)
from .forms import ArticlesCreateForm
from .utils import *


def zip_list(lst, sz):
    return [lst[i::sz] for i in range(sz)]


class CategoriesIndex(DataMixin, ListView):
    model = Categories
    template_name = 'categories/index.html'
    context_object_name = 'categories'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = zip_list(
            context['categories'],
            2
        )
        default_context = self.get_user_context(
            active_menu='categories_index',
            title='Categories'
        )
        return dict(list(context.items()) + list(default_context.items()))

    def get_queryset(self):
        return Categories.objects\
            .annotate(total=Count('articles', filter=Q(articles__is_published=True)))\
            .filter(is_published=True, total__gt=0)\
            .order_by('-priority', 'name')


class CategoriesView(DataMixin, DetailView):
    model = Categories
    template_name = 'categories/view.html'
    context_object_name = 'category'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = zip_list(
            self.get_object().articles_set.filter(is_published=True).order_by('time_create'),
            2
        )
        default_context = self.get_user_context(
            title='Categories'
        )
        return dict(list(context.items()) + list(default_context.items()))

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect('categories_index')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ArticlesCreate(LoginRequiredMixin, DataMixin, CreateView):
    form_class = ArticlesCreateForm
    template_name = 'articles/create.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        default_context = self.get_user_context(
            active_menu='articles_create',
            title='Categories'
        )
        return dict(list(context.items()) + list(default_context.items()))
