from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
LISTEN = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')    
)

class Album(models.Model):
    name = models.CharField(max_length=25)
    covercolor = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('albums_detail', kwargs={'pk': self.id})

class Song(models.Model):
    song = models.CharField(max_length=100)
    genre = models.TextField(max_length=100)
    rating = models.IntegerField()
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.song

    def get_absolute_url(self):
        return reverse('detail', kwargs={'song_id': self.id})

    def listen_for_today(self):
        return self.listening_set.filter(date=date.today()).count() >= len(LISTEN)

class Listening(models.Model):
    date = models.DateField('listening date')
    listen = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=LISTEN,
        # set the default value for meal to be 'B'
        default=LISTEN[0][0]
    )
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_listen_display()} on {self.date}"

    class Meta:
        ordering = ['-date']