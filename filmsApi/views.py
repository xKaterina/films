from rest_framework.generics import ListCreateAPIView
import urllib.request
from filmsApi.models import Film, Omdb
from filmsApi.serializer import FilmSerializer
import json


class CreateView(ListCreateAPIView):
    """

    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def upload(request):
        omdbId = Omdb.objects.filter(flag=False)
        print(omdbId[0])
        response = urllib.request.urlopen('http://www.omdbapi.com/?i='+str(omdbId[0])+'&plot=full&apikey=a03f8aac')
        film = json.loads(response.read())

        newFilm = Film()
        newFilm.title = film['Title']
        newFilm.year = film['Year']
        newFilm.rated = film['Rated']
        newFilm.released = film['Released']
        newFilm.runtime = 90
        newFilm.slogan = film['Year']
        newFilm.genre = film['Genre']
        newFilm.director = film['Director']
        newFilm.writer = film['Writer']
        newFilm.actors = film['Actors']
        newFilm.plot = film['Plot']
        newFilm.language = film['Language']
        newFilm.country = film['Country']
        newFilm.production = film['Production']
        newFilm.boxOffice = film['BoxOffice']
        newFilm.poster = film['Poster']
        newFilm.save()

        id = Omdb.objects.get(omdbId=omdbId[0].omdbId)
        id.flag = True
        id.save()

        return super()

    def createFilm(self, film):
        newFilm = Film()
        newFilm.title = film['Title']
        newFilm.year = film['Year']
        newFilm.rated = film['Rated']
        newFilm.released = film['Released']
        newFilm.runtime = 90
        newFilm.slogan = film['Year']
        newFilm.genre = film['Genre']
        newFilm.director = film['Director']
        newFilm.writer = film['Writer']
        newFilm.actors = film['Actors']
        newFilm.plot = film['Plot']
        newFilm.language = film['Language']
        newFilm.country = film['Country']
        newFilm.production = film['Production']
        newFilm.boxOffice = film['BoxOffice']
        newFilm.poster = film['Poster']
        newFilm.save()