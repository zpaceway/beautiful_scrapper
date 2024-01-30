from django.db import models


class Image(models.Model):
    service_name = models.CharField(max_length=128)
    url = models.URLField(unique=True)

    class Meta:
        unique_together = (
            "service_name",
            "url",
        )

    def __str__(self) -> str:
        return self.url


class Search(models.Model):
    text = models.CharField(max_length=128)
    images = models.ManyToManyField(Image, related_name="searches")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text
