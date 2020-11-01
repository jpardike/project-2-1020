from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='images/city_pics/', null=True)
    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length = 100)
    current_city = models.ForeignKey(City, on_delete = models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/profile_pics/', default = "images/profile_pics/profile_placeholder.jpg")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length = 250)
    content = models.TextField(max_length = 1000)
    date = models.DateField()
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/post_pics/', null = True)
    def __str__(self):
        return self.title
