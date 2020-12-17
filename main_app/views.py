from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Song, Album
from .forms import ListeningForm


# Define the home view
class SongCreate(CreateView):
    model = Song
    fields = '__all__'

# Create your views here.
class SongUpdate(UpdateView):
  model = Song
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['genre', 'rating']

class SongDelete(DeleteView):
  model = Song
  success_url = '/songs/'


def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def songs_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', { 'songs': songs })

def songs_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    albums_song_doesnt_have = Album.objects.exclude(id__in = song.albums.all().values_list('id'))
    listening_form = ListeningForm()
    return render(request, 'songs/detail.html', { 
        'song': song, 'listening_form': listening_form,
        'albums': albums_song_doesnt_have
    })

def add_listening(request, song_id):
  # create a ModelForm instance using the data in request.POST
  form = ListeningForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_listening = form.save(commit=False)
    new_listening.song_id = song_id
    new_listening.save()
  return redirect('detail', song_id=song_id)

def assoc_album(request, song_id, album_id):
  Song.objects.get(id=song_id).albums.add(album_id)
  return redirect('detail', song_id=song_id)

class AlbumList(ListView):
  model = Album

class AlbumDetail(DetailView):
  model = Album

class AlbumCreate(CreateView):
  model = Album
  fields = '__all__'

class AlbumUpdate(UpdateView):
  model = Album
  fields = ['name', 'covercolor']

class AlbumDelete(DeleteView):
  model = Album
  success_url = '/albums/'