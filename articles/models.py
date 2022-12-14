from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from pytils.translit import translify


class Categories(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    priority = models.PositiveIntegerField(default=0)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('categories_view', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-priority', '-time_create']


class Articles(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255, db_index=True)
    content = models.TextField()
    cover = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('categories_view', kwargs={'category_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = translify(slugify(self.title, allow_unicode=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-time_create', 'title']
