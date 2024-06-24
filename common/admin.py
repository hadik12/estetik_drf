from django.contrib import admin

from common.models import *


class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'file_type']
    list_display_links = ['file']


admin.site.register(CommonSettings)
admin.site.register(Media, MediaAdmin)
