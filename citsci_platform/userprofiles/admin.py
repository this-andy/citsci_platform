from django.contrib import admin

# Register your models here.
from .models import UserProfile, NHSStaffProfile

admin.site.register(UserProfile)
admin.site.register(NHSStaffProfile)
