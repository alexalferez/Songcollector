from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('songs/', views.songs_index, name='index'),
    path('songs/<int:song_id>', views.songs_detail, name='detail'),
    path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
    path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
    path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
    path('songs/<int:song_id>/add_listening/', views.add_listening, name='add_listening'),
    path('songs/<int:song_id>/assoc_album/<int:album_id>/', views.assoc_album, name='assoc_album'),
    path('albums/', views.AlbumList.as_view(), name='albums_index'),
    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name='albums_detail'),
    path('albums/create/', views.AlbumCreate.as_view(), name='albums_create'),
    path('albums/<int:pk>/update', views.AlbumUpdate.as_view(), name='albums_update'),
    path('albums/<int:pk>/delete', views.AlbumDelete.as_view(), name='albums_delete'),
]