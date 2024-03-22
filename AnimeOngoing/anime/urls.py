from django.urls import path
from rest_framework import routers

from .views import AnimeViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r'animes', AnimeViewSet, basename='animes')
# router.register(r'users', UserViewSet)


urlpatterns = []

urlpatterns += router.urls
