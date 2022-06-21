from django.urls import path
from articles.views import *

urlpatterns = [
    path('', index),
    path('categories/', categories),
    path('test/', test),
]