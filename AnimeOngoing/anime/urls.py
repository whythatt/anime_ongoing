from rest_framework import routers

from .views import AnimeListView, FavoriteAnimeViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r'animes', AnimeListView)
router.register(r'users', UserViewSet)
router.register(r'favorite', FavoriteAnimeViewSet, basename='favorite')

urlpatterns = router.urls
