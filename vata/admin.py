from django.contrib import admin
from .models import Movie, Genre, Types, AddComments

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Note the comma

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Note the comma

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Note the comma

@admin.register(AddComments)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Note the comma