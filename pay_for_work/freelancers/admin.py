from django.contrib import admin
from .models import freelancer,projectbids
# Register your models here.


class freelancerAdmin(admin.ModelAdmin):
    pass
    list_display=('first_name', 'email', 'contact_number','is_verified','status','joined_date')
    search_fields = ("first_name",)
    list_filter = ('first_name','skills')
    prepopulated_fields = {'slug':('first_name','last_name',)}
    ordering = ["-id"]
    #list_editable = ("status",)  
    fieldsets = (
        ('Basic Informations', {
        'fields': ('first_name','last_name','slug', 'email', 'contact_number','image',)
        }),
        ('Details and Skills', {
        'classes': ('wide',),
        'fields': ('skills', 'more_info',),
        }),        
        ('Status', {
        'classes': ('wide',),
        'fields': ('joined_date','blocked_date','is_verified','status',),
        }),
        )  
admin.site.register(freelancer, freelancerAdmin)


class projectbidAdmin(admin.ModelAdmin):
    pass
    list_display=('project_id', 'freelancer_id', 'bid_date',)
    search_fields = ("project_id",)
    list_filter = ('project_id','freelancer_id',)
    #prepopulated_fields = {'slug':('first_name','last_name',)}
    ordering = ["-id"]
    #list_editable = ("status",)  
    fieldsets = (
        ('Bid Informations :', {
        'fields': ('project_id','freelancer_id','bid_date',)
        }),        
        )  
admin.site.register(projectbids, projectbidAdmin)