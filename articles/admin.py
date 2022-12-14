from django.contrib import admin
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
    list_display = ('title', 'slug', 'content', 'is_published')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)
