from rest_framework import routers

from .views import ViewAnimeList

router = routers.SimpleRouter()
router.register(r'animes', ViewAnimeList)

urlpatterns = router.urls
