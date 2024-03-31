from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ShortenedURL(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='shortened')
    original_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.original_url} -------> {self.short_url}'
