from django.db import models
from django.db.models.query_utils import Q
from accounts.models import User
class Benefactor(models.Model):
    experience_choices = (
        (0, 'low'),
        (1, 'moderate'),
        (2, 'high')
    )
    
    id = models.AutoField(primary_key= True, unique= True, blank= False, null= False)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    experience = models.SmallIntegerField(choices= experience_choices, default= 0)
    free_time_per_week = models.PositiveSmallIntegerField(default= 0)


class Charity(models.Model):
    id = models.AutoField(primary_key= True, unique= True, blank= False, null= False)
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length= 10)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user:User):
        queryset = self.filter(charity__user__id= user.id)
        return queryset
    
    def related_tasks_to_benefactor(self, user:User):
        queryset = self.filter(assigned_benefactor__user__id= user.id)
        return queryset
    
    def all_related_tasks_to_user(self, user:User):
        return self.filter(
            Q(state= 'P') |
            Q(charity__user__id= user.id) |
            Q(assigned_benefactor__user__id= user.id))


class Task(models.Model):
    objects = TaskManager()
    
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    state_choices = (
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done'),
    )
    
    id = models.AutoField(primary_key= True, unique= True, blank= False, null= False)
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete= models.SET_NULL, null= True, blank= True)
    charity = models.ForeignKey(Charity, on_delete= models.CASCADE)
    age_limit_form = models.IntegerField(null= True, blank= True)
    age_limit_to = models.IntegerField(null= True, blank= True)
    date = models.DateField(null= True, blank= True)
    description = models.TextField(null= True, blank= True)
    gender_limit = models.CharField(choices= gender_choices, max_length=1, null= True, blank= True)
    state = models.CharField(choices= state_choices, max_length=50, default= 'D')
    title = models.CharField(max_length= 100)
