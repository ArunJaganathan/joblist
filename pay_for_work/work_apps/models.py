from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    STATUS_OBJ = (
        ('1', 'Active'),
        ('2', 'In Active'),
        ('3', 'Draft'),
    ) 

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_OBJ,blank=True,null=True)
    date=models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.name



class Technology(models.Model):
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    STATUS_OBJ = (
        ('1', 'Active'),
        ('2', 'In Active'),
        ('3', 'Draft'),
    ) 
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    status = models.CharField(max_length=2, choices=STATUS_OBJ,blank=True,null=True)
    date=models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.name       



class Location(models.Model):
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    STATUS_OBJ = (
        ('1', 'Active'),
        ('2', 'In Active'),
    ) 
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_OBJ,blank=True,null=True)
    date=models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.name          

class Jobtype(models.Model):
    class Meta:
        verbose_name = "Job type"
        verbose_name_plural = "Job Nature"

    STATUS_OBJ = (
        ('1', 'Active'),
        ('2', 'In Active'),
    ) 
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_OBJ,blank=True,null=True)
    date=models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.name        