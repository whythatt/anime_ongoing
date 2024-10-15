import aiohttp
import asyncio
import concurrent.futures
import json
import os
import re
import timeit

import requests
from lxml import etree

from date_formatting import date_form


async def get_anime_links(session, page):
    url = f"https://animeschedule.net/shows?mt=all&airing-statuses-exclude=Finished&page={page}"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    all_anime_links = []

    async with session.get(url=url, headers=headers) as response:
        response = await response.text()
        tree = etree.fromstring(response, etree.HTMLParser())

        anime_block = tree.xpath('//div[@class="anime-tile lozad"]')
        for mediatype in anime_block:
            if (
                mediatype.xpath("@mediatypes")[0] == "tv"
                or mediatype.xpath("@mediatypes")[0] == "movie"
            ):
                anime_link = "https://animeschedule.net" + mediatype.xpath("@itemid")[0]
                all_anime_links.append(anime_link)
            else:
                continue

    return all_anime_links


async def fetch_anime_data(session, anime_link, anime_data_list):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    async with session.get(url=anime_link, headers=headers) as response:
        if response.status == 200:
            data = await response.text()
            tree = etree.fromstring(data, etree.HTMLParser())

            title = tree.xpath('//*[@id="anime-header-main-title"]/text()')[0]

            image_url = tree.xpath('//*[@id="anime-poster"]')
            image_url = image_url[0].attrib["src"]
            pic_name = f"anime_pics/{clean_anime_title(title)}.jpg"

            # союираю данные из блока с данными об аниме. Все это из одной пременной - data_block_data
            data_block_data = tree.xpath('//section[@id="information-section-large"]')[
                0
            ]

            mediatype = data_block_data.xpath('.//div/h3[text()="Type"]')
            mediatype = check(mediatype, "Type", xpath="..//a/text()")

            total_episodes = data_block_data.xpath('.//div/h3[text()="Episodes"]')
            total_episodes = check(total_episodes, "Episodes", xpath="../div/text()")
            # делаю числом если не None
            if total_episodes:
                total_episodes = int(total_episodes)

            season = data_block_data.xpath('.//div/h3[text()="Season"]')
            season = check(season, "Season", xpath="../a/text()")

            release_date = data_block_data.xpath('.//div/h3[text()="Release Date"]')
            release_date = check(release_date, "Release Date", xpath="../time/text()")

            status = data_block_data.xpath('.//div/h3[text()="Status"]')
            status = check(status, "Status", xpath="../div/text()")

            episode_duration = data_block_data.xpath(
                './/div/h3[text()="Episode Length"]'
            )
            episode_duration = check(
                episode_duration, "Episode Length", xpath="../div/text()"
            )

            score = data_block_data.xpath('.//div/h3[text()="Score"]')
            score = check(score, "Score", xpath="../strong/text()")
            if score:
                score = float(score)

            description = data_block_data.xpath('//*[@id="description"]/p/text()')
            if description:
                description = description[0].strip()
            else:
                description = None

            release_time_block = tree.xpath('//*[@id="release-times-section"]')
            if len(release_time_block) > 0:
                release_time_block = release_time_block[0]

                next_episode_count = release_time_block.xpath(
                    '//span[@class="release-time-episode-number"]/text()'
                )[0].split(" ")[1]

                release_date_next_ep = release_time_block.xpath(
                    '//*[@class="release-time"]'
                )[0].get("datetime")
                # форматирую полученную строку времени нужный мне формат
                release_date_next_ep = date_form(release_date_next_ep)
            else:
                next_episode_count = None
                release_date_next_ep = None

            anime_data = {
                "title": title.strip(),
                "image_url": image_url,
                "pic_name": pic_name,
                "next_episode_count": next_episode_count,
                "total_episodes": total_episodes,
                "release_date_next_ep": release_date_next_ep,
                "mediatype": mediatype,
                "season": season,
                "release_date": release_date,
                "status": status,
                "episode_duration": episode_duration,
                "score": score,
                "description": description,
            }
            anime_data_list.append(anime_data)
        else:
            return None


async def gather_data():
    url = "https://animeschedule.net/shows?mt=all&airing-statuses-exclude=Finished"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        tree = etree.fromstring(await response.text(), etree.HTMLParser())
        all_page_count = tree.xpath('//*[@id="last-page"]/text()')[0]

        tasks = [
            asyncio.create_task(get_anime_links(session, page))
            for page in range(1, int(all_page_count) + 1)
        ]

        await asyncio.gather(*tasks)

        all_anime_links = []

        for task in tasks:
            all_anime_links.extend(await task)

        anime_data_list = []

        fetch_tasks = [
            asyncio.create_task(fetch_anime_data(session, link, anime_data_list))
            for link in all_anime_links
        ]

        await asyncio.gather(*fetch_tasks)

        clean_anime_pics_folder("/home/whythat/python/anime_ongoing/frontend/public")

        # Save images after fetching data
        await save_anime_pics(anime_data_list)

        with open("anime_data_async.json", "w", encoding="utf-8") as json_file:
            json.dump(anime_data_list, json_file, ensure_ascii=False, indent=4)


def check(block, text, xpath):
    if len(block) > 0:
        if block[0].text == f"{text}":
            return block[0].xpath(xpath)[0]
    else:
        block = None
        return block


def clean_anime_title(title):
    title = title.replace("/", "_")
    title = title.replace(":", "_")
    title = title.replace(" ", "_")
    title = title.replace("?", "")
    title = title.replace("!", "")
    title = title.replace("#", "")
    title = title.replace(".", "")
    title = re.sub("_+", "_", title)

    return title


async def download_image(session, url, filename):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                with open(filename, "wb") as file:
                    file.write(await response.read())
            else:
                print(
                    f"[ERROR] Failed to download {filename}: Status code {response.status}"
                )
    except Exception as err:
        print(f"[ERROR] Не удалось загрузить {filename}: {err}")


async def save_anime_pics(anime_data_list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for item in anime_data_list:
            image_url = item["image_url"]
            pic_name = item["pic_name"]
            filename = f"/home/whythat/python/anime_ongoing/frontend/public/{pic_name}"
            tasks.append(download_image(session, image_url, filename))
        await asyncio.gather(*tasks)


def clean_anime_pics_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    asyncio.run(gather_data())
