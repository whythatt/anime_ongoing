from django.urls import path
from rest_framework import routers

from .views import AnimeViewSet, FavoriteAnimeViewSet

router = routers.SimpleRouter()
router.register(r"animes", AnimeViewSet, basename="animes")


urlpatterns = [
    path(
        "favorites/",
        FavoriteAnimeViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "favorites/<int:pk>/",
        FavoriteAnimeViewSet.as_view({"get": "retrieve", "delete": "destroy"}),
    ),
]

urlpatterns += router.urls
