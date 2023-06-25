from django.db import models
from django.db.models import Model
from tinymce import models as tinymce_models
from work_apps import models as PREFERENCE
from projects import models as PROJECTS

# Create your models here.



class freelancer(models.Model):
    class Meta:
        verbose_name = "Freelancer Desk"
        verbose_name_plural = "Manage Freelancer"

    STATUS_OBJ = (  
        ('1', 'Active'),
        ('2', 'Inactive'),       
        ('3', 'Draft'),
    ) 
    VERIFY_OBJ = (  
        ('1', 'Verified'),
        ('2', 'Not Verified'),       
        ('3', 'Blocked'),
    )

    first_name = models.CharField(max_length=100,help_text ='*First name is very important !')
    last_name = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(
        max_length = 200,
        unique = True,
        verbose_name = 'Mail ID',
        error_messages ={ "unique":"Email you entered is not unique."}
        )
    contact_number = models.CharField(max_length=30)    
    more_info = tinymce_models.HTMLField(blank=True, null=True) 
    #skills=models.ManyToManyField(PREFERENCE.Technology)
    skills=models.ForeignKey(PREFERENCE.Technology, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)    
    joined_date=models.DateField()
    blocked_date=models.DateField(blank=True, null=True)
    is_verified = models.CharField(max_length=2, choices=VERIFY_OBJ)
    #status = models.CharField(max_length=2, choices=STATUS_OBJ,blank=True,null=True)
    #status = models.CharField(choices=STATUS_OBJ, widget=models.RadioSelect())
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    status = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    

    def __str__ (self):
        return self.first_name



class projectbids(models.Model):
    class Meta:
        verbose_name = "Project Bids"
        verbose_name_plural = "Manage Bids"   

    project = models.ForeignKey(PROJECTS.Projectdata, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(freelancer, on_delete=models.CASCADE)  
    bid_date=models.DateField() 