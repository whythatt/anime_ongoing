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


async def fetch_anime_data(session, anime_link):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    async with session.get(url=anime_link, headers=headers) as response:
        if response.status == 200:
            data = await response.text()
            tree = etree.fromstring(data, etree.HTMLParser())
            title = tree.xpath('//*[@id="anime-header-main-title"]/text()')
            return {"link": anime_link, "title": title}
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

        fetch_tasks = [
            asyncio.create_task(fetch_anime_data(session, link))
            for link in all_anime_links
        ]

        anime_data_results = await asyncio.gather(*fetch_tasks)

        for result in anime_data_results:
            if result:
                print(result)


if __name__ == "__main__":
    asyncio.run(gather_data())
