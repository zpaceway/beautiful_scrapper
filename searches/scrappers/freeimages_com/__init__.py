from typing import List
from slugify import slugify
import requests
from bs4 import BeautifulSoup
from searches.utils import remove_query_params_from_url
import math
from threading import Thread
import promisipy


def scrape_images_from_freeimages_com(search: str, limit: str) -> List[str]:
    # define freeimage.com
    base_url = "https://www.freeimages.com/search"
    items_per_page = 60

    number_of_pages = math.ceil(limit / items_per_page)

    def get_images_from_page(page):
        slugified_seach = slugify(search)
        query_url = f"{base_url}/{slugified_seach}/{page}"
        response = requests.get(query_url)
        soup = BeautifulSoup(response.text, "html.parser")
        images = soup.find_all(
            "img",
            class_="grid-thumb",
            src=lambda value: value
            and value.startswith("https://images.freeimages.com/"),
        )
        return list(map(lambda img: remove_query_params_from_url(img["src"]), images))

    image_urls = []

    promises = [
        promisipy.Promise(
            lambda page=page: get_images_from_page(page), mode="threading"
        ).start()
        for page in range(1, number_of_pages + 1)
    ]

    for promise in promises:
        image_urls.extend(promise.wait().result)

    return image_urls[:limit]
