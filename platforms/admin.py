from django.contrib import admin
from django.contrib.contenttypes import generic
from .models import Platform, PlatformObject, Resolution
from . import settings as platforms_settings


class PlatformObjectInline(generic.GenericTabularInline):
    model = PlatformObject
    extra = 1
    verbose_name = 'Platform'
    verbose_name_plural = 'Platforms'

if platforms_settings.USE_PLATFORMS:
	admin.site.register(Platform)
	admin.site.register(Resolution)
