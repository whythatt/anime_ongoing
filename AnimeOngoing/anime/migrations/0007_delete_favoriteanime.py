# Generated by Django 5.0.2 on 2024-03-21 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_alter_anime_next_episode_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FavoriteAnime',
        ),
    ]
