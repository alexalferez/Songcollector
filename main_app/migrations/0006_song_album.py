# Generated by Django 3.1.4 on 2020-12-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ManyToManyField(to='main_app.Album'),
        ),
    ]
