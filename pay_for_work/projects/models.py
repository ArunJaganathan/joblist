from django.db import models
from tinymce import models as tinymce_models
from work_apps import models as PREFERENCE
# Create your models here.


class Projectowner(models.Model):
    class Meta:
        verbose_name = "Project-Owner"
        verbose_name_plural = "Owner"

    STATUS_OBJ = (  
        ('1', 'Active'),
        ('2', 'Inactive'),       
        ('3', 'Draft'),
    ) 

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True)
    icon = models.ImageField(upload_to="images", blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_OBJ,blank=True,null=True)
    date=models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.name

class Projectdata(models.Model):
    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"

    STATUS_OBJ = (  
        ('1', 'Active'),
        ('2', 'Inactive'),       
        ('3', 'Draft'),       
              
    ) 

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    owner =models.ForeignKey(Projectowner, on_delete=models.CASCADE)
    category=models.ForeignKey(PREFERENCE.Category, on_delete=models.CASCADE)
    technology=models.ForeignKey(PREFERENCE.Technology, on_delete=models.CASCADE)
    job_type=models.ForeignKey(PREFERENCE.Jobtype, on_delete=models.CASCADE)
    short_description = tinymce_models.HTMLField()    
    #project_bid_start_date=models.DateTimeField(auto_now_add = True)
    #project_bid_end_date=models.DateTimeField(auto_now_add = True)
    description = tinymce_models.HTMLField()    
    added_date=models.DateTimeField(auto_now_add = True)
    project_bid_start_date=models.DateField()
    project_bid_end_date=models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_OBJ,blank=True,null=True)

    def __str__ (self):
        return self.name[:5]
    def show_desc(self):
        return self.short_description[:50]    