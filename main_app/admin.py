from django.contrib import admin

# Register your models here.
from .models import Song, Listening, Album

admin.site.register(Song)
admin.site.register(Listening)
admin.site.register(Album)