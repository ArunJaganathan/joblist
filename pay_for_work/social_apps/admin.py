from django.contrib import admin
from .models import SocialPlugin
# Register your models here.


class SocialPluginAdmin(admin.ModelAdmin):
    pass
    list_display=('name','status','date')
    search_fields = ("status",)
    list_filter = ('status',)
admin.site.register(SocialPlugin, SocialPluginAdmin)