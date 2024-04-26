from authorization.models import MyUser
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Anime, FavoriteAnime
from .serializers import AnimeSerializer, FavoriteAnimeSerializer


# Create your views here.
class AnimeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Anime.objects.all().order_by("id")
        serializer = AnimeSerializer(queryset, many=True)
        return Response(serializer.data)


class FavoriteAnimeViewSet(viewsets.ViewSet):
    serializer_class = FavoriteAnimeSerializer

    def list(self, request):
        queryset = FavoriteAnime.objects.all()
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
