menu = [
    {
        'title': 'Home',
        'index': 'home',
        'url_name': 'index'
    },
    {
        'title': 'Create article',
        'index': 'articles_create',
        'url_name': 'articles_create',
        'needs_auth': True
    }
]

submenu = [
    {
        'title': 'Categories',
        'index': 'categories_index',
        'url_name': 'categories_index'
    },
    {
        'title': 'Test',
        'index': 'test',
        'url_name': 'test'
    },
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        context['submenu'] = submenu

        if 'active_menu' not in kwargs:
            context['active_menu'] = None

        context = self.check_for_auth(context)

        return context

    def check_for_auth(self, context):
        is_auth = self.request.user.is_authenticated

        context['menu'] = self.check_menu(context['menu'], is_auth)
        context['submenu'] = self.check_menu(context['submenu'], is_auth)

        context['pages_view_range_limit'] = 2
        context['pages_view_range_limit_neg'] = -context['pages_view_range_limit']

        return context

    def check_menu(self, menu_to_check, is_auth):
        menu_cp = menu_to_check.copy()
        for menu_item in menu_cp:
            if menu_item.get('needs_auth') and not is_auth:
                menu_cp.remove(menu_item)
        return menu_cp
