# TODO : Complete Signals Account
from django.db.models.expressions import F
from django.dispatch import receiver
from django.db.models.signals import m2m_changed, post_init, post_save
from .models import User, Profile, Website
from django.db.models.functions import Concat
from django.db.models import Value, F

@receiver(post_save, sender= User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ouruser = Profile.objects.create(user= instance)
        ouruser.save()
    
    
@receiver(m2m_changed, sender= Website.users.through)
def update_bio(sender, instance, **kwargs):
    # if a user adds a website then the instance is User
    if kwargs['reverse'] == True and kwargs['action'] == 'post_add':
        profile = Profile.objects.get(user__id= instance.id)
        websites = Website.objects.filter(users= instance)\
            .values_list('url', flat= True).order_by('url')
        websites_formatted = '\n'.join(websites)
        profile.bio = websites_formatted
        profile.save()

    # if a website has a new user then the instance is Website
    if kwargs['reverse'] == False and kwargs['action'] == 'post_add' :
        # profile = Profile.objects.get(user__id= instance.)
        # latest_user = User.objects.latest('id')
        # profile = Profile.objects.get(user__id= latest_user.id)
        # websites = Website.objects.filter(users= latest_user).values_list('url', flat= True)
        # websites_formatted = '\n'.join(websites)
        # profile.bio = websites_formatted
        # profile.save()
        # profiles = Profile.objects.filter(user__id__in= kwargs['pk_set'])
        for user in kwargs['pk_set']:
            profile = Profile.objects.filter(user__id= user)
            websites = Website.objects.filter(users__id= user)\
                .values_list('url', flat= True).order_by('url')
            websites_formatted = '\n'.join(websites)
            
            profile.update(bio= Value(websites_formatted))
            
            
            
            
            # websites = Website.objects.filter(users__id= user).values_list('url', flat= True)
            # websites_formatted = '\n'.join(websites)
            # profile.bio = websites_formatted
            # profile.save()
            
            # profile.bio




