from django.contrib import admin

from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_published', 'priority')
    list_display_links = ('name', 'slug')
    search_fields = ('name', 'slug')
    list_editable = ('is_published', 'priority')
    list_filter = ('is_published', 'priority', 'time_create')
    prepopulated_fields = {'slug': ('name',)}


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'is_published')
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Articles, ArticlesAdmin)
