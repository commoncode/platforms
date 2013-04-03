# -*- coding: utf-8 -*-
from entropy.base import OrderingMixin, SlugMixin, TitleMixin, AttributeMixin

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Platform(TitleMixin, SlugMixin, AttributeMixin):
    """A platform.
    """
    # title and short_title from TitleMixin
    # slug from SlugMixin

    # TODO add 'canonical' FK relationship to canonical Platform.
    pass


class PlatformObject(models.Model):
    """A Generic relation between objects and Platforms.
    """
    platform = models.ForeignKey(Platform)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()

    def __unicode__(self):
        return self.platform.title


class PlatformObjectManager(models.Manager):
    """An object manager to be used by publishable objects.
    """
    def platform(self, platform):
        """Returns a QuerySet for the base Model, limited to ids of
        instances related to the supplied Platform.
        """
        ctype = ContentType.objects.get_for_model(self.model)
        return self.get_query_set().filter(
            id__in=PlatformObject.objects.filter(
                platform=platform,
                content_type=ctype
            ).values_list('object_id', flat=True))


class Resolution(OrderingMixin):
    """Different ways we might resolve to a Platform instance.
    """
    # order from OrderingMixin
    platform = models.ForeignKey(Platform)
    domain = models.CharField(max_length=255, blank=True,
        help_text="Start with . to match subdomains e.g. .domain.com to match this.domain.com and www.domain.com")
    subdomain = models.CharField(max_length=255, blank=True)
    uripattern = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return "domain: {}, order: {}".format(self.domain, self.order)


    class Meta:
        ordering = ['order',]
