from authorization.models import MyUser
from django.contrib import admin

from .models import Anime

# Register your models here.
admin.site.register(Anime)
admin.site.register(MyUser)
