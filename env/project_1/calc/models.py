from django.db import models

# Create your models here.
class data(models.Model):
    code = models.CharField(max_length=100)       
    name = models.CharField(max_length=100)               
    branch = models.CharField(max_length=100) 
    semester = models.CharField(max_length=100)   
    credit = models.IntegerField()
    faculty = models.CharField(max_length=100)           
    theory = models.IntegerField()
    tutorial = models.IntegerField()
    lab = models.IntegerField()
    lab_name = models.CharField(max_length=100) 
