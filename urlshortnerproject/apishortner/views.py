from django.shortcuts import render
from .serializers import ShortenedURLSerializer
from shortner.models import ShortenedURL
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

# search filter
from rest_framework.filters import SearchFilter


class ShortendUrlViewset(viewsets.ModelViewSet):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
    filter_backends = (SearchFilter, )
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    pagination_class = PageNumberPagination




