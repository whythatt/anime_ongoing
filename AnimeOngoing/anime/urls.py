from django.urls import path
from rest_framework import routers

from .views import (AddFavoriteAnime, AnimeListView, FavoriteAnimeList,
                    UserViewSet)

router = routers.SimpleRouter()
router.register(r'animes', AnimeListView)
router.register(r'users', UserViewSet)
# router.register(r'favorite_list', FavoriteAnimeListViewSet, basename='favorite_list')
# router.register(r'favorite_create', FavoriteAnimeCreateView.as_view(), basename='favorite_create')


urlpatterns = [
    path('favorite_anime/', FavoriteAnimeList.as_view()),
    path('add_favorite_anime/', AddFavoriteAnime.as_view()),
]

urlpatterns += router.urls
