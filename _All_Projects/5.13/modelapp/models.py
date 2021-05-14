from django.db import models


class BookManager(models.Manager):
    def sort_by_rate(self):
        return self.order_by('-rate')


class Book(models.Model):
    name = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    free = models.BooleanField(default=True)

    # CONFIG YOUR MODEL MANAGER HERE
    objects = BookManager
    
    def __str__(self):
        return self.name
