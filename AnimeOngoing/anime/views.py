from authorization.models import MyUser
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Anime, FavoriteAnime
from .serializers import AnimeSerializer, FavoriteAnimeSerializer


# Create your views here.
class AnimeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Anime.objects.all().order_by('id')
        serializer = AnimeSerializer(queryset, many=True)

        return Response(serializer.data)

class FavoriteAnimeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = FavoriteAnime.objects.all()
        serializer = FavoriteAnimeSerializer(queryset, many=True)
        return Response(serializer.data)
