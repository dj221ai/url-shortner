from rest_framework import serializers
from shortner.models import ShortenedURL


class ShortenedURLSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortenedURL
        fields = ['id', 'original_url', 'short_url', 'created_at']
