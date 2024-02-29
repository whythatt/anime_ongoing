from django.shortcuts import render
from rest_framework import viewsets

from .models import Anime
from .serializers import AnimeSerializer


# Create your views here.
class ViewAnimeList(viewsets.ReadOnlyModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
