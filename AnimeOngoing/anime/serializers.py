from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Anime, FavoriteAnime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False, required=True)
    username = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class FavoriteAnimeListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    anime = AnimeSerializer()
    class Meta:
        model = FavoriteAnime
        fields = '__all__'

    def get_user(self, obj):
        return obj.user
    
    def get_anime(self, obj):
        return obj.anime

class FavoriteAnimeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteAnime
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        anime = validated_data['anime']
        favorite_anime = FavoriteAnime.objects.create(user=user, anime=anime)
        return favorite_anime
