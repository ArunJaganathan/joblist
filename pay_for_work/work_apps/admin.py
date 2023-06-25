from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.html import format_html
from .models import Category,Technology,Location,Jobtype
# Register your models here.

@admin.action(description='Active',)
def make_active(modeladmin, request, queryset):
    queryset.update(status = 1)
@admin.action(description='In Active',)
def make_inactive(modeladmin, request, queryset):
    queryset.update(status = 2)
class CategoryAdmin(admin.ModelAdmin):
    pass
    list_display=('name','status','date')
    search_fields = ("name",)
    list_filter = ('status',)
    actions = [make_active, make_inactive]
admin.site.register(Category, CategoryAdmin)

class TechnologyAdmin(admin.ModelAdmin):
    pass
    list_display=('name','status','date','Icon')
    search_fields = ("name",)
    list_filter = ('status',)
    def Icon(self, obj):
        return mark_safe(f'<img src="/{obj.image}" width="100"/>')
admin.site.register(Technology, TechnologyAdmin)

class LocationAdmin(admin.ModelAdmin):
    pass
    list_display=('name','status','date')
    search_fields = ("name",)
    list_filter = ('status',)
admin.site.register(Location, LocationAdmin)

class JobtypeAdmin(admin.ModelAdmin):
    pass
    list_display=('name','status','date')
    search_fields = ("name",)
    list_filter = ('status',)
admin.site.register(Jobtype, JobtypeAdmin)