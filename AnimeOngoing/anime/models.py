from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=500)
    next_episode_count = models.CharField(max_length=10, blank=True, null=True)
    total_episodes = models.IntegerField(blank=True, null=True)
    release_date_next_ep = models.CharField(max_length=100, blank=True, null=True)
    mediatype = models.CharField(max_length=10, blank=True, null=True)
    season = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100)
    episode_duration = models.CharField(max_length=100, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} | {self.status} | {self.mediatype}"
