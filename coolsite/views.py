from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from articles.utils import *
from coolsite.forms import RegisterUserForm


class IndexView(DataMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        default_context = self.get_user_context(
            active_menu='home',
            title='Home'
        )
        return dict(list(context.items()) + list(default_context.items()))


class TestView(DataMixin, TemplateView):
    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        default_context = self.get_user_context(
            active_menu='test',
            title='Test'
        )
        return dict(list(context.items()) + list(default_context.items()))


class RegisterView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        default_context = self.get_user_context(
            active_menu='register',
            title='register'
        )
        return dict(list(context.items()) + list(default_context.items()))

# def test(request):
#     args = {
#         'active_menu': 'test',
#         'menu': menu,
#         'submenu': submenu,
#     }
#     return render(request, 'test.html', args)
