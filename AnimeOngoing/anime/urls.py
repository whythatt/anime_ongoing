from django.urls import path
from rest_framework import routers

from .views import AnimeViewSet, FavoriteAnimeViewSet

router = routers.SimpleRouter()
router.register(r'animes', AnimeViewSet, basename='animes')


urlpatterns = [
    path('favorites_list/', FavoriteAnimeViewSet.as_view({'get': 'list'})),
    path('favorites_add/', FavoriteAnimeViewSet.as_view({'post': 'create'})),
    path('favorites_delete/', FavoriteAnimeViewSet.as_view({'delete': 'destroy'})),
]

urlpatterns += router.urls
