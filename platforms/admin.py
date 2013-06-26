from django.contrib import admin
from django.contrib.contenttypes import generic
from entropy.admin import InlineAttributeAdmin
from .models import Platform, PlatformObject, Resolution
from . import settings


class PlatformSetting(InlineAttributeAdmin):
    verbose_name = "Platform Setting"
    verbose_name_plural = verbose_name + 's'


class PlatformObjectInline(generic.GenericTabularInline):
    model = PlatformObject
    extra = 1
    verbose_name = 'Platform'
    verbose_name_plural = 'Platforms'


class ResolutionInline(admin.TabularInline):
    model = Resolution
    extra = 1

class ResolutionAdmin(admin.ModelAdmin):
    list_display = ('platform', 'domain',)


class PlatformAdmin(admin.ModelAdmin):
    inlines = [PlatformSetting, ResolutionInline]


if settings.USE_PLATFORMS:
    admin.site.register(Platform, PlatformAdmin)
    admin.site.register(Resolution, ResolutionAdmin)
