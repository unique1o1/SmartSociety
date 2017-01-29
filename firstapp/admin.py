from django.contrib import admin
from .models import item
# Register your models here.
class itemadmin(admin.ModelAdmin):
	list_display=('title', 'amount')
admin.site.register(item, itemadmin)