# Generated by Django 5.0.2 on 2024-04-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_delete_favoriteanime'),
        ('authorization', '0002_myuser_favorite_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='favorite_anime',
            field=models.ManyToManyField(to='anime.anime'),
        ),
    ]
