from django.contrib import admin

from .models import (Gallery)

class GalleryAdmin(admin.ModelAdmin):
    model=Gallery
    list_display = ['uploaded', 'pic']

admin.site.register(Gallery, GalleryAdmin)