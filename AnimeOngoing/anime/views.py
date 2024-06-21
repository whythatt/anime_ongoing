from authorization.models import MyUser
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Anime, FavoriteAnime
from .serializers import AnimeSerializer, FavoriteAnimeSerializer


# Create your views here.
class AnimeViewSet(viewsets.ViewSet):
    def list(self, request):
        search_query = request.GET.get("search")
        sort_query = request.GET.get("sortBy")
        if search_query and sort_query:
            queryset = Anime.objects.filter(title__icontains=search_query).order_by(
                sort_query
            )
        elif search_query:
            queryset = Anime.objects.filter(title__icontains=search_query)
        elif sort_query:
            queryset = Anime.objects.all().order_by(sort_query)
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
