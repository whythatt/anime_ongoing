# Generated by Django 5.0.3 on 2024-06-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0008_favoriteanime'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='updated',
            field=models.BooleanField(default=False),
        ),
    ]
