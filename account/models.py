from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    picture = models.ImageField(upload_to='files/profile', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_pi')