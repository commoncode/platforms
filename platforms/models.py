# -*- coding: utf-8 -*-
from entropy.base import OrderingMixin, SlugMixin, TitleMixin

from django.db import models


class Platform(TitleMixin, SlugMixin):
    """A platform.
    """
    # title and short_title from TitleMixin
    # slug from SlugMixin

    # TODO add 'canonical' FK relationship to canonical Platform.
    pass


# class PlatformManager(models.Manager):
#     """An object manager to be used by publishable objects.
#     """
#     pass


class Resolution(OrderingMixin):
    """Different ways we might resolve to a Platform instance.
    """
    # order from OrderingMixin
    platform = models.ForeignKey(Platform)
    domain = models.CharField(max_length=255, blank=True)
    subdomain = models.CharField(max_length=255, blank=True)
    uripattern = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return "domain: {}, order: {}".format(self.domain, self.order)


    class Meta:
        ordering = ['order',]
