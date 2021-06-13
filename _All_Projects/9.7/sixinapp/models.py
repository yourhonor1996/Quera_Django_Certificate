from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    num_stars = models.IntegerField()
