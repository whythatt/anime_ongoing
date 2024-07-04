import json

from django.core.management.base import BaseCommand

from anime.models import Anime


class Command(BaseCommand):
    help = "Load anime data from JSON file into the database"

    def handle(self, *args, **options):
        with open("../parsing_anime_data/anime_data.json", "r") as file:
            data = json.load(file)  # Получаем все объекты Anime из базы данных
            all_anime = Anime.objects.all()
            for item in data:
                # Поиск объекта с таким же title в базе данных
                try:
                    anime = all_anime.get(title=item["title"])
                    if (
                        anime.total_episodes != item["total_episodes"]
                        or anime.status != item["status"]
                        or anime.score != item["score"]
                    ):
                        # Обновление измененных полей объекта
                        anime.next_episode_count = item["next_episode_count"]
                        anime.total_episodes = item["total_episodes"]
                        anime.release_date_next_ep = item["release_date_next_ep"]
                        anime.status = item["status"]
                        anime.score = item["score"]
                        anime.save()
                    elif (
                        anime.next_episode_count != item["next_episode_count"]
                        or anime.release_date_next_ep != item["release_date_next_ep"]
                    ):
                        anime.next_episode_count = item["next_episode_count"]
                        anime.release_date_next_ep = item["release_date_next_ep"]
                        anime.updated = True
                        anime.save()
                    else:
                        anime.updated = False
                        anime.save()
                except Anime.DoesNotExist:
                    # Создание нового объекта, если не найден существующий
                    Anime.objects.create(
                        title=item["title"],
                        pic_name=item["pic_name"],
                        next_episode_count=item["next_episode_count"],
                        total_episodes=item["total_episodes"],
                        release_date_next_ep=item["release_date_next_ep"],
                        mediatype=item["mediatype"],
                        season=item["season"],
                        release_date=item["release_date"],
                        status=item["status"],
                        episode_duration=item["episode_duration"],
                        score=item["score"],
                        description=item["description"],
                        updated=False,
                    )
            # Удаление аниме, которых нет в json фале
            Anime.objects.exclude(title__in=[item["title"] for item in data]).delete()

        self.stdout.write(self.style.SUCCESS("Data updated successfully"))
