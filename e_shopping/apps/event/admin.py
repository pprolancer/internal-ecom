from django.contrib import admin

# Register your models here.
from event.models import (Event)

class EventAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return True

admin.site.register(Event)
