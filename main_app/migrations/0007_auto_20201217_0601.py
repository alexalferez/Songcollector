# Generated by Django 3.1.4 on 2020-12-17 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_song_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='album',
            new_name='albums',
        ),
    ]
