from django.conf import settings
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, db_index=True)
    text = models.TextField(blank=True, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Hotel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
