from django.urls import path
from rest_framework import routers

from .views import AnimeViewSet, FavoriteAnimeViewSet

router = routers.SimpleRouter()
router.register(r'animes', AnimeViewSet, basename='animes')
router.register(r'add_favorite_anime', FavoriteAnimeViewSet, basename='favorite_animes')


urlpatterns = []

urlpatterns += router.urls
