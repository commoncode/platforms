from django.contrib import admin
from django.contrib.contenttypes import generic
from .models import Platform, PlatformObject, Resolution


class PlatformObjectInline(generic.GenericTabularInline):
    model = PlatformObject
    extra = 1
    verbose_name = 'Platform'
    verbose_name_plural = 'Platforms'


admin.site.register(Platform)
admin.site.register(Resolution)
