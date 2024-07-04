import json

import requests


def get_anime_data(url):
    """Получаю данные об аниме"""
    my_list = []
    for i in range(1, 1000):
        try:
            res = requests.get(url.format(num=i))
            my_list.append(res.json())
        except requests.exceptions.JSONDecodeError:
            return my_list


# urls for api requests
movie_url = "https://animeschedule.net/api/v3/anime?page={num}&mt=all&media-types=movie&airing-statuses-exclude=finished"
tv_url = "https://animeschedule.net/api/v3/anime?page={num}&mt=all&media-types=tv&airing-statuses-exclude=finished"

# сохраняю данные в список
anime_data = []
print("getting movie")
anime_data.append({"mediatypes_movie": get_anime_data(url=movie_url)})
print("getting tv")
anime_data.append({"mediatypes_tv": get_anime_data(url=tv_url)})

# Сохранить данные об аниме в файл
with open("data_from_api.json", "w") as f:
    json.dump(anime_data, f, indent=4)
