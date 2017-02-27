from django.contrib import admin
from .models import item, slot
# Register your models here.


class itemadmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'message', 'id')
admin.site.register(item, itemadmin)


class slotadmin(admin.ModelAdmin):
    list_display = ('id', 'slotno', 'slotid', 'times')
admin.site.register(slot, slotadmin)
