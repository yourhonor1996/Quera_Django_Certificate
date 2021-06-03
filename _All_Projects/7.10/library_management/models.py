from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    available = models.BooleanField(default=False, null=True, blank=True)
