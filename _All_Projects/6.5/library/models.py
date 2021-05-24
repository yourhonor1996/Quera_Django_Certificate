from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        formatter = 'Name: {:28} | Written by: {:8} | Price: {:6}'
        return formatter.format(self.name, self.author, self.price)
