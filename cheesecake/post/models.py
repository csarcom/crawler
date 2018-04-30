from django.db import models


class Post(models.Model):
    title = models.TextField('title',)
    author = models.CharField('author', max_length=100)
    intro = models.TextField('intro',)
    post_url = models.URLField('post_url', unique=True)
    category = models.CharField('category', max_length=100)
    author_url = models.URLField('author_url',)
    date = models.CharField('date', max_length=100)
