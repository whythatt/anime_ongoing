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

    def create(self, validated_data):
        anime_id = validated_data.pop("anime")
        user_id = validated_data.pop("user")

        anime = Anime.objects.get(id=anime_id)

        favorite = FavoriteAnime.objects.create(anime=anime, user=user_id)
        return favorite
