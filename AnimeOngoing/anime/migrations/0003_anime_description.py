# Generated by Django 5.0.2 on 2024-02-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_alter_anime_next_episode_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
