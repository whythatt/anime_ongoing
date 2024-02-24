import json

from django_app.AnimeOngoing.anime import Anime

with open('anime_data.json', 'r') as file:
    data = json.load(file)

    for i in data:
        anime = Anime(
            title=i['title'],
            next_episode_count=i['next_episode_count'],
            total_episodes=i['total_episodes'],
            release_date_next_ep=i['release_date_next_ep'],
            mediatype=i['mediatype'],
            season=i['season'],
            release_date=i['release_date'],
            status=i['status'],
            episode_duration=i['episode_duration'],
            score=i['score'],
        )
        anime.save()
