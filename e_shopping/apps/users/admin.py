from django.contrib import admin

# Register your models here.

from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "user_role", "product_count","product_price_limit")
    def has_add_permission(self, request, obj=None):
        return False

# admin.site.register(Parents)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Relationship)

