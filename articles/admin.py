from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_published', 'get_html_image', 'priority')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_editable = ('is_published', 'priority')
    list_filter = ('is_published', 'priority', 'time_create')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('slug', 'name', 'image', 'get_html_image', 'priority', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_image')

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=100>')

    get_html_image.short_description = 'image'


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'link_to_category', 'link_to_author', 'content', 'is_published')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'slug', 'content')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    def link_to_category(self, obj):
        link = reverse("admin:articles_categories_change", args=[obj.category.id])
        return format_html('<a href="{}">{}</a>', link, obj.category.name)

    link_to_category.short_description = 'Category'

    def link_to_author(self, obj):
        link = reverse("admin:auth_user_change", args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', link, obj.author.username)

    link_to_author.short_description = 'Author'


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)
