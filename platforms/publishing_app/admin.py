from django.contrib import admin
from platforms.admin import PlatformObjectInline
from .models import MyPost


class MyPostAdmin(admin.ModelAdmin):
    inlines = [PlatformObjectInline,]


admin.site.register(MyPost, MyPostAdmin)
