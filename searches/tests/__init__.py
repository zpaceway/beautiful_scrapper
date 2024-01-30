from django.test import TestCase
from searches.tests.utils import (
    get_mocked_scrape_100_images_response_from_freeimages_com,
    mocked_scrape_images_from_freeimages_com_get_request,
)
from searches.utils import remove_query_params_from_url, save_images_from_search
from searches.scrappers.freeimages_com import scrape_images_from_freeimages_com
from unittest import mock
import os


class ScrapperUtilsTestCase(TestCase):
    def test_remove_query_params_from_url(self):
        url = "https://google.com?this=is"
        result = remove_query_params_from_url(url)
        self.assertEqual(result, "https://google.com")

    def test_save_images_from_search(self):
        search_text = "test-search"
        service_name = "test-service"
        image_urls = [
            "https://example.com/example1.jpg",
            "https://example.com/example2.jpg",
            "https://example.com/example3.jpg",
            "https://example.com/example1.jpg",
        ]
        search, images = save_images_from_search(search_text, image_urls, service_name)

        self.assertEqual(len(images), 3)
        self.assertEqual(search.images.count(), 3)


class ScrapperTestCase(TestCase):
    @mock.patch("requests.get", mocked_scrape_images_from_freeimages_com_get_request)
    def test_scrape_images_from_freeimages_com(
        self,
    ):
        search = "dogs"
        limit = 100
        images = scrape_images_from_freeimages_com(search, limit)

        self.assertEqual(
            images, get_mocked_scrape_100_images_response_from_freeimages_com()
        )
