from django.contrib import admin
from django.urls import path

from searches.views import scrape_images_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("scrape/images/<str:service_name>/", scrape_images_view),
]
