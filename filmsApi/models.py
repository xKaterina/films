from django.db import models


class Film(models.Model):
    title = models.CharField('Название', max_length=200, null=True)
    year = models.IntegerField('Год', null=True)
    rated = models.CharField('Рейтинг', max_length=15, null=True)
    released = models.CharField('Дата релиза', max_length=25, null=True)
    runtime = models.IntegerField('Время', null=True)
    slogan = models.CharField('Слоган', max_length=200, null=True)
    genre = models.CharField('Жанр', max_length=50, null=True)
    director = models.CharField('Режисер', max_length=50, null=True)
    writer = models.CharField('Сценарист', max_length=50, null=True)
    actors = models.CharField('Актеры', max_length=100, null=True)
    plot = models.CharField('Описание', max_length=250, null=True)
    language = models.CharField('Язык', max_length=30, null=True)
    country = models.CharField('Страна', max_length=25, null=True)
    production = models.CharField('Продакшн компания', max_length=30, null=True)
    boxOffice = models.CharField('Прокат', max_length=20, null=True)
    poster = models.CharField('URL-постер', max_length=100, null=True)

    def __str__(self):
        return self.title


class Omdb(models.Model):
    omdbId = models.CharField('omdbId',  max_length=50)
    flag = models.BooleanField('flag')

    def __str__(self):
        return self.omdbId
