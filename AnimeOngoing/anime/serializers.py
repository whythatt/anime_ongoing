from rest_framework import serializers

from authorization.models import MyUser

from .models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

class FavoriteAnimeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    anime_id = serializers.IntegerField()

class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(allow_blank=False, required=True)
    # username = serializers.CharField(max_length=100)
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'username', 'favorite_anime', 'password')
