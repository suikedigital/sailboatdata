from django.contrib import admin

from .models import SailData, Boat

# Register your models here.

admin.site.register(Boat)
admin.site.register(SailData)