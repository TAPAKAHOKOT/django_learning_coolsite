from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
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
    Categories
)
from .forms import ArticlesCreateForm
from .utils import *


def zip_list(lst, sz):
    return [lst[i::sz] for i in range(sz)]


class CategoriesIndex(DataMixin, ListView):
    paginate_by = 4
    model = Categories
    template_name = 'categories/index.html'
    context_object_name = 'categories'
    # allow_empty = False

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

        articles = context['object'].articles_set.filter(is_published=True).order_by('time_create')
        paginator = Paginator(articles, 4)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)

        context['page_obj'] = page_object
        context['articles'] = zip_list(
            page_object,
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.is_published = True
        return super(ArticlesCreate, self).form_valid(form)
