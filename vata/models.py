from django.db import models
from datetime import date
import urllib.parse as urlparse
from urllib.parse import parse_qs


# Create your models here.

class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Types(models.Model):
    name = models.CharField("Имя", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name  # исправлено

    class Meta:
        verbose_name = "Тип контента"
        verbose_name_plural = "Типы контента"


class Movie(models.Model):  # добавлено наследование от models.Model
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="posters/%Y")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2024)
    country = models.CharField("Страна", max_length=30)
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    url = models.URLField()
    types = models.ManyToManyField(Types, verbose_name="Тип контента")

    def __str__(self):
        return self.title

    def youtube_id(self):
        query = urlparse.urlparse(self.url).query
        params = parse_qs(query)
        return params.get('v', [None])[0]

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class AddComments(models.Model):
    name = models.CharField('Имя', max_length=50)
    text_comments = models.CharField('Текст комментария', max_length=400)
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.name} on {self.movie.title}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
