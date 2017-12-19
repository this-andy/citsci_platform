from django.contrib import admin
from .models import Photo

# Register your models here.


class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Photo, PhotoAdmin)
