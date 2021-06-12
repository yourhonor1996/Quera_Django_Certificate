from django.db import models


class Person(models.Model):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    full_name = models.CharField(max_length=60)
    height = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    age = models.IntegerField()

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.full_name, self.height, self.gender, self.age)
