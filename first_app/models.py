from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField("name var", max_length=70)
    age = models.IntegerField("integer var")    
    country = models.IntegerField("country field")