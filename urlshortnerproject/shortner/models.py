from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.original_url} converted to {self.short_url}'
