from django.db import models

# Create your models here.


class SocialPlugin(models.Model):
    class Meta:
        verbose_name = "Social Plugin"
        verbose_name_plural = "Social Plugin"

    STATUS_OBJ = (  
        ('1', 'Facebook'),
        ('2', 'Twitter'),       
        ('3', 'Instagram'),       
        ('4', 'Linked In'),       
    ) 

    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="images", blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_OBJ,blank=True,null=True)
    date=models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.name