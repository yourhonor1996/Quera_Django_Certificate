from django.db import models


class User(models.Model):
    name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    score = models.IntegerField()

    def change_name(self, new_name):
        self.name = new_name
        self.save()

    def change_password(self, new_password):
        self.password = new_password
        self.save()

    def change_score(self, x):
        self.score += x
        self.save()

    def __str__(self):
        return self.name
