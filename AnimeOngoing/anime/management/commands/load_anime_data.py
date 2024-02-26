import json

from anime.models import Anime
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load anime data from JSON file into the database'

    def handle(self, *args, **options):
        with open('../parsing_anime_data/anime_data.json', 'r') as file:
            data = json.load(file)
            # Получаем все объекты Anime из базы данных
            all_anime = Anime.objects.all()
            for item in data:
                # Поиск объекта с таким же title в базе данных
                anime = all_anime.filter(title=item['title']).first()
                if anime:
                    # Обновление существующего объекта
                    anime.title = item['title']
                    anime.next_episode_count = item['next_episode_count']
                    anime.total_episodes = item['total_episodes']
                    anime.release_date_next_ep = item['release_date_next_ep']
                    anime.mediatype = item['mediatype']
                    anime.season = item['season']
                    anime.release_date = item['release_date']
                    anime.status = item['status']
                    anime.episode_duration = item['episode_duration']
                    anime.score = item['score']
                    anime.description = item['description']
                    anime.save()
                else:
                    # Создание нового объекта, если не найден существующий
                    Anime.objects.create(
                        title = item['title'],
                        next_episode_count = item['next_episode_count'],
                        total_episodes = item['total_episodes'],
                        release_date_next_ep = item['release_date_next_ep'],
                        mediatype = item['mediatype'],
                        season = item['season'],
                        release_date = item['release_date'],
                        status = item['status'],
                        episode_duration = item['episode_duration'],
                        score = item['score'],
                        description = item['description'],
                    )
        
        self.stdout.write(self.style.SUCCESS('Data updated successfully'))
