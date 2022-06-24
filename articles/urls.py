from django.conf.urls.static import static
from django.urls import path
from articles.views import *
from coolsite import settings

urlpatterns = [
    path('', index),
    path('categories/', categories, name="categories"),
    path('categories/<str:category_slug>/', category_index),
    path('test/', test),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)