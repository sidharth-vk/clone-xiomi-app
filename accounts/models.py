from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    image = models.ImageField( upload_to="profile_image" , default="default.webp")
    bio = models.CharField(("welcome to mi"),max_length=50)
    
    def __str__(self):
        return f'{self.user.username} Profile '
    
    