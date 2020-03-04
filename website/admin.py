from django.contrib import admin

from website.models import WebsiteUser, Video


@admin.register(WebsiteUser)
class WebsiteUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['filename', 'user']
