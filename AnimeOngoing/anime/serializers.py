from rest_framework import serializers

from .models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

class FavoriteAnimeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    anime_id = serializers.IntegerField()
