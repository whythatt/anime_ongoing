from django.contrib.auth.models import User
# from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

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

class FavoriteAnimeList(generics.ListAPIView):
    queryset = FavoriteAnime.objects.all()
    serializer_class = FavoriteAnimeSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user.id
        return FavoriteAnime.objects.filter(user=user)

class AddFavoriteAnime(generics.CreateAPIView):
    def perform_create(self, serializer):
        user = self.request.user
        anime = self.request.data.get('anime')
        serializer.save(user=user, anime=anime)

# class FavoriteAnimevViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = FavoriteAnimeListSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return FavoriteAnime.objects.filter(user=user)
#
# class FavoriteAnimeCreateView(generics.CreateAPIView):
#     queryset = FavoriteAnime.objects.all()
#     serializer_class = FavoriteAnimeCreateSerializer
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         anime = self.request.data.get('anime')
#         serializer.save(user=user, anime=anime)
