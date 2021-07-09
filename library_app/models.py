from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    pages_count = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Profile(models.Model):
    """Model definition for Profile."""

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    
    phone_number = models.CharField(blank= True, null= True, max_length=50)
    country = models.CharField(max_length=100)

    class Meta:
        """Meta definition for Profile."""
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        pass
