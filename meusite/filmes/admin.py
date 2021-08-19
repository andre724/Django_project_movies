from .models import Filme
from django.contrib import admin

# Register your models here.


class FilmeAdmin(admin.ModelAdmin):
    list_display = ('movie_title','image_tag')

admin.site.register(Filme, FilmeAdmin)