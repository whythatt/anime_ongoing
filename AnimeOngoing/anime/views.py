from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Anime, FavoriteAnime
from .serializers import AnimeSerializer, FavoriteAnimeSerializer


# Create your views here.
class AnimeViewSet(viewsets.ViewSet):
    def list(self, request):
        search = request.GET.get("search")
        filter = request.GET.get("filter")
        if search and (filter == "movie" or filter == "tv"):
            queryset = Anime.objects.filter(
                title__icontains=search, mediatype__icontains=filter
            )
        elif search and (
            filter == "ongoing" or filter == "upcoming" or filter == "delayed"
        ):
            queryset = Anime.objects.filter(
                title__icontains=search, status__icontains=filter
            )
        elif search:
            queryset = Anime.objects.filter(title__icontains=search)
        elif filter == "movie" or filter == "tv":
            queryset = Anime.objects.filter(mediatype__icontains=filter)
        elif filter == "ongoing" or filter == "upcoming" or filter == "delayed":
            queryset = Anime.objects.filter(status__icontains=filter)
        else:
            queryset = Anime.objects.all().order_by("id")
        serializer = AnimeSerializer(queryset, many=True)
        return Response(serializer.data)


class FavoriteAnimeViewSet(viewsets.ViewSet):
    serializer_class = FavoriteAnimeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavoriteAnime.objects.filter(user=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = FavoriteAnimeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        anime_id = request.data.get("anime_id")

        favorite_anime = FavoriteAnime.objects.create(
            user_id=request.user.id, anime_id=anime_id
        )
        serializer = FavoriteAnimeSerializer(favorite_anime)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        favorite_anime = get_object_or_404(queryset, pk=pk)
        serializer = FavoriteAnimeSerializer(favorite_anime)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        favorite_anime = get_object_or_404(queryset, pk=pk)
        favorite_anime.delete()
        return Response({"message": "Anime was deleted <3"}, status=204)
