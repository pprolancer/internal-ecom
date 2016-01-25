from django.contrib import admin

# Register your models here.

from .models import *

# admin.site.register(Parents)
admin.site.register(UserProfile)
admin.site.register(Relationship)

