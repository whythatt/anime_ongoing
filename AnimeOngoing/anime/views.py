from django.contrib.auth.models import User
# from django.shortcuts import render
from rest_framework import viewsets

from .models import Anime, FavoriteAnime
from .serializers import (AnimeSerializer, FavoriteAnimeSerializer,
                          UserSerializer)


# Create your views here.
class AnimeListView(viewsets.ReadOnlyModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FavoriteAnimeViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteAnimeSerializer
   
    def get_queryset(self):
        user = self.request.user
        return FavoriteAnime.objects.filter(user=user)
