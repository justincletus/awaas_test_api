from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio             = models.TextField(max_length=500, blank=True, null=True)
    location        = models.CharField(max_length=50, blank=True, null=True)
    birth_date      = models.DateField(null=True, blank=True, help_text="format : DD-MM-YYYY")
    email_confirmed = models.BooleanField(default=False)
    image           = models.ImageField(default='default.jpg', upload_to='profile_pic')
    token           = models.CharField(max_length=200, blank=True, null=True)
    is_active       = models.BooleanField(default=False, null=True)    
    
    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
