from django.db import models

from platforms.models import PlatformObjectManager


class MyPost(models.Model):
    slug = models.SlugField()
    body = models.TextField()

    objects = PlatformObjectManager()

    def __unicode__(self):
        return self.slug
