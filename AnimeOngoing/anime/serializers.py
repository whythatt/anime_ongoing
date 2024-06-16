from rest_framework import serializers

from .models import Anime, FavoriteAnime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = "__all__"


class FavoriteAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteAnime
        fields = "__all__"
