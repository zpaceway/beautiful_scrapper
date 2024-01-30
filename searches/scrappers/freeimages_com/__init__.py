from typing import List
from slugify import slugify
import requests
from bs4 import BeautifulSoup
from searches.utils import remove_query_params_from_url
import math
from threading import Thread


def scrape_images_from_freeimages_com(search: str, limit: str) -> List[str]:
    # define freeimage.com
    base_url = "https://www.freeimages.com/search"
    items_per_page = 60

    number_of_pages = math.ceil(limit / items_per_page)

    image_urls = []

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
        new_image_urls = list(
            map(lambda img: remove_query_params_from_url(img["src"]), images)
        )
        image_urls.extend(new_image_urls)

    tasks = []

    for page in range(1, number_of_pages + 1):
        task = Thread(target=get_images_from_page, args=[page])
        tasks.append(task)

    for task in tasks:
        task.start()

    for task in tasks:
        task.join()

    return image_urls[:limit]
