from django.contrib import admin
import csv
from .models import Projectdata,Projectowner
# Register your models here.

@admin.action(description="Generate CSV")
class ProjectdataAdmin(admin.ModelAdmin):
    pass
    list_display=('name','owner','technology','job_type','category','status','added_date')
    search_fields = ("status","name",)
    list_filter = ('owner_id','status','technology','job_type','category',)
    prepopulated_fields = {'slug':('name',)}
    ordering = ["-id"]
    #list_editable = ("status",)  
    fieldsets = (
        ('Project Informations :', {
        'fields': ('name','slug', 'technology', 'category',)
        }),
        ('Project Owner Details :', {
        'classes': ('wide',),
        'fields': ('owner', 'job_type',),
        }),
        ('Project More Informations : ', {
        'classes': ('wide',),
        'fields': ('short_description','description',),
        }),
        ('Project Status : ', {
        'classes': ('wide',),
        'fields': ('project_bid_start_date','project_bid_end_date','status',),
        }),
        )  
    """ def generateCSV(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;   filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

        list_display = ['name', 'status']
        ordering = ['name']
        actions = [generateCSV] """
admin.site.register(Projectdata, ProjectdataAdmin)


class ProjectownerAdmin(admin.ModelAdmin):
    pass
    list_display=('name','status','date')
    search_fields = ("status",)
    list_filter = ('status',)
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Projectowner, ProjectownerAdmin)