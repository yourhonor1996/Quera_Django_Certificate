from django.db import models
# imports here
from django.contrib.auth.models import AbstractUser


# write your models here
class CustomUser(AbstractUser):
    national_code = models.EmailField(max_length= 10, unique= True)
    height = models.FloatField()
    father_name = models.CharField(max_length= 50)
    