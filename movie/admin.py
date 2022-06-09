from django.contrib import admin
from .models import GenreModel, MovieModel

# Register your models here.
admin.site.register(GenreModel)
admin.site.register(MovieModel)

