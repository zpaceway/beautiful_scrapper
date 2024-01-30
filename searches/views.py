from searches.scrappers.freeimages_com import scrape_images_from_freeimages_com
from django.http import JsonResponse

from searches.utils import save_images_from_search


def scrape_images_view(request, service_name):
    search = request.GET.get("search")
    limit = int(request.GET.get("limit"))

    if not search or not limit:
        return JsonResponse(
            {
                "status": "error",
                "reason": "search and limit query params must not be empty",
            },
            status=400,
        )

    if service_name == "freeimages.com":
        images = scrape_images_from_freeimages_com(search, limit)
        save_images_from_search(search, images, service_name)

    return JsonResponse(
        {
            "images": images,
            "count": len(images),
        }
    )
