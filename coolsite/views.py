from django.views.generic import TemplateView
from django.shortcuts import render
from articles.utils import *


class IndexView(DataMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        default_context = self.get_user_context(
            active_menu='home',
            title='Home'
        )
        return dict(list(context.items()) + list(default_context.items()))


def test(request):
    args = {
        'active_menu': 'test',
        'menu': menu,
        'submenu': submenu,
    }
    return render(request, 'test.html', args)

