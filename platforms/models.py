# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from entropy.base import OrderingMixin, SlugMixin, TitleMixin, AttributeMixin


class Platform(TitleMixin, SlugMixin, AttributeMixin):
    '''
    Platform.

    '''
    # title
    # short_title
    # slug

    pass



class Resolution(OrderingMixin):
    '''
    If Platforms are used in a Request / Response context, we can use Resolutions
    to determine which Platform we're dealing with.

    '''

    # order

    platform = models.ForeignKey('Platform')
    domain = models.CharField(
        max_length=256,
        blank=True,
        help_text="Start with . to match subdomains e.g. .domain.com to match this.domain.com and www.domain.com")
    subdomain = models.CharField(
        max_length=256,
        blank=True)
    uripattern = models.CharField(
        max_length=256,
        blank=True)

    def __unicode__(self):
        return "domain: {}, order: {}".format(self.domain, self.order)


    class Meta:
        ordering = ['order',]
