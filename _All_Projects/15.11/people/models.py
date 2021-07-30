from django.db import models


class Person(models.Model):
    fullname = models.CharField(max_length=250, null=True)
    information = models.CharField(max_length=350, null=True)

