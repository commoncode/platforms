from django.contrib import admin
from django.contrib.contenttypes import generic
from .models import Platform, PlatformObject, Resolution
from . import settings


class PlatformObjectInline(generic.GenericTabularInline):
    model = PlatformObject
    extra = 1
    verbose_name = 'Platform'
    verbose_name_plural = 'Platforms'


class PlatformInlineMixin(object):
    """A mixin to add the platform inline based on user settings
    """
    def __init__(self, model, admin_site):
        # Check to see if platforms is installed, and if it is,
        # whether or not to use it in the admin
        try:
            if settings.USE_PLATFORMS:
                self.__class__.inlines += [PlatformObjectInline,]
        except NameError:
            pass 
        super(PlatformInlineMixin, self).__init__(model, admin_site)


if settings.USE_PLATFORMS:
    admin.site.register(Platform)
    admin.site.register(Resolution)
