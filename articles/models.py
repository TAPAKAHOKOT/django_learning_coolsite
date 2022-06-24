from django.db import models


class Categories(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    priority = models.PositiveIntegerField(default=0)

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.slug
