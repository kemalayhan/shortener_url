from django.db import models

from shortener.utils import create_short_url


class UrlShortener(models.Model):
    url = models.CharField(max_length=10000)
    short_url = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.short_url} - {self.url}"

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_short_url(self)
        super(UrlShortener, self).save(*args, **kwargs)