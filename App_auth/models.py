from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Song(models.Model):
    
    name = models.CharField(max_length=200)
    song_img = models.FileField()
    singer = models.CharField(max_length=200)
    song_file = models.FileField()

    def __str__(self):
        return self.name
class Image(models.Model):
    img = models.FileField()

