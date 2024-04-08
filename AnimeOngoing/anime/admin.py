from django.contrib import admin

from .models import Anime, FavoriteAnime

# Register your models here.
admin.site.register(Anime)
admin.site.register(FavoriteAnime)
