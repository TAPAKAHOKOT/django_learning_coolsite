from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import (
    DetailView,
    ListView
)
from articles.models import (
    Categories,
    Articles
)


def zip_list(lst, sz):
    return [lst[i::sz] for i in range(sz)]


class CategoriesIndex(ListView):
    model = Categories
    template_name = 'categories/index.html'
    context_object_name = 'categories'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = zip_list(context['categories'], 2)
        return context

    def get_queryset(self):
        return Categories.objects.filter(is_published=True).order_by('-priority', 'name')


class CategoriesView(DetailView):
    model = Categories
    template_name = 'categories/view.html'
    context_object_name = 'category'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = zip_list(
            Articles.objects.filter(category_id=self.get_object().id).order_by('time_create'),
            2
        )
        return context

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect('categories_index')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
