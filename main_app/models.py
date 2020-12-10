from django.db import models

# Create your models here.

class Song(models.Model):
    song = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.TextField(max_length=100)
    rating = models.IntegerField()