import os
import json

dirname, _ = os.path.split(os.path.abspath(__file__))


def mocked_scrape_images_from_freeimages_com_get_request(*args, **kwargs):
    class MockResponse:
        _text = ""

        def __init__(self, html) -> None:
            self._text = html

        @property
        def text(self):
            return self._text

    mocked_html_1 = ""
    mocked_html_2 = ""
    with open(f"{dirname}/assets/test_dogs_search_page_1.html") as f1:
        mocked_html_1 = f1.read()
    with open(f"{dirname}/assets/test_dogs_search_page_2.html") as f2:
        mocked_html_2 = f2.read()

    if args[0] == "https://www.freeimages.com/search/dogs/1":
        return MockResponse(mocked_html_1)
    elif args[0] == "https://www.freeimages.com/search/dogs/2":
        return MockResponse(mocked_html_2)

    return MockResponse(None, 404)


def get_mocked_scrape_100_images_response_from_freeimages_com():
    images = []
    with open(f"{dirname}/assets/images_100.json") as file:
        images = json.load(file)["images"]

    return images
