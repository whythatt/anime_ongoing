from authorization.models import MyUser
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Anime
from .serializers import AnimeSerializer, UserSerializer


# Create your views here.
class AnimeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Anime.objects.all()
        serializer = AnimeSerializer(queryset, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
