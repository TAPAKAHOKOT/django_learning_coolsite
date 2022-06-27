from django.conf.urls.static import static
from django.urls import path
from articles.views import *
from coolsite import settings

urlpatterns = [
    path('categories/', CategoriesIndex.as_view(), name="categories_index"),
    path('categories/<str:category_slug>/', CategoriesView.as_view(), name="categories_view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
