"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from coolsite.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('test/', TestView.as_view(), name='test'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('', include('articles.urls')),
    path('admin/', admin.site.urls, name='admin'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handle404 = pageNotFound
