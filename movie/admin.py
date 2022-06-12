from django.contrib import admin
from .models import GenreModel, MovieModel, MovieComment

# Register your models here.
admin.site.register(GenreModel)
admin.site.register(MovieModel)
admin.site.register(MovieComment)
