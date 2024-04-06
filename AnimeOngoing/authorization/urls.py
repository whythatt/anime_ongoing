from django.urls import path
from rest_framework import routers

from .views import MyUserViewSet

router = routers.SimpleRouter()
router.register(r'users/me', MyUserViewSet, basename='user_data')

urlpatterns = []

urlpatterns += router.urls
