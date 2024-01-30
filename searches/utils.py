from typing import List
from searches.models import Image, Search


def remove_query_params_from_url(url: str) -> str:
    return url.split("?")[0]


def save_images_from_search(search_text: str, image_urls: List[str], service_name: str):
    existing_images = Image.objects.filter(
        url__in=image_urls, service_name=service_name
    ).values_list("url", flat=True)

    existing_images_set = set(existing_images)
    image_urls_to_create = set(image_urls) - existing_images_set

    Image.objects.bulk_create(
        [Image(url=url, service_name=service_name) for url in image_urls_to_create]
    )

    images = Image.objects.filter(
        url__in=image_urls,
        service_name=service_name,
    ).only("id")
    search = Search.objects.create(text=search_text)
    search.images.add(*images)

    return search, images
