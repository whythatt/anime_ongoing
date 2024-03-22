from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Anime


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
