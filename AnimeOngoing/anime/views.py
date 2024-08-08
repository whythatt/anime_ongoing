from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    def list(self, request):
        user = request.user
        queryset = FavoriteAnime.objects.filter(user=user)
        serializer = FavoriteAnimeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        anime_id = request.data.get("anime_id")
        user_id = request.user.id
        favorite_anime = FavoriteAnime.objects.create(
            anime_id=anime_id, user_id=user_id
        )
        serializer = self.serializer_class(favorite_anime)
        return Response(serializer.data)

    def destroy(self, request, anime_id=None):
        anime_id = request.data.get("anime_id")
        user_id = request.user.id
        favorite_anime = FavoriteAnime.objects.filter(
            anime_id=anime_id, user_id=user_id
        )
        favorite_anime.delete()
        return Response(f"anime was deleted <3")
