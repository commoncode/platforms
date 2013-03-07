from django.contrib import admin
from django.contrib.contenttypes import generic
from .models import Platform, PlatformObject, Resolution
from . import settings


class PlatformObjectInline(generic.GenericTabularInline):
    model = PlatformObject
    extra = 1
    verbose_name = 'Platform'
    verbose_name_plural = 'Platforms'


class ResolutionAdmin(admin.ModelAdmin):
    list_display = ('platform', 'domain',)


if settings.USE_PLATFORMS:
    admin.site.register(Platform)
    admin.site.register(Resolution, ResolutionAdmin)
