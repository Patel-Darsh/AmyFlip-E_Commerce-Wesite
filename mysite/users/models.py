from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    location = models.CharField(default = 'Location', max_length = 100)
    user_type_choices = (
        ('admin', 'admin'),
        ('com_owner', 'com_owner'),
        ('cust', 'cust')
    )
    user_type = models.CharField(max_length = 100, choices = user_type_choices, blank = False)
    def __str__(self):
        return self.user.username