from authorization.models import MyUser
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Anime
from .serializers import (AnimeSerializer, FavoriteAnimeSerializer,
                          UserSerializer)


# Create your views here.
class AnimeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Anime.objects.all()
        serializer = AnimeSerializer(queryset, many=True)

        return Response(serializer.data)

class FavoriteAnimeViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = FavoriteAnimeSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data.get('user_id')
            anime_id = serializer.validated_data.get('anime_id')

            user = MyUser.objects.get(id=user_id)
            user.favorite_anime.add(anime_id)
            user.save()
            return Response({'message': 'Аниме успешно добавлено в избранное'}, status=201)
        else:
            return Response(serializer.errors, status=400)

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
