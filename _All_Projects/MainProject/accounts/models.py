from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.AutoField(primary_key= True, unique= True, blank= False, null= False)
    address = models.TextField(blank=True,null=True)
    age = models.PositiveSmallIntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F','Female'),
    )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)

