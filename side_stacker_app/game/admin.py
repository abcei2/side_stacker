from django.contrib import admin

# Register your models here.
from game.models import TemporalGame
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(TemporalGame)
