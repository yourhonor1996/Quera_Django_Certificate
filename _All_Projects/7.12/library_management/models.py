from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
