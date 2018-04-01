from rest_framework.generics import ListCreateAPIView
import urllib.request
from filmsApi.models import Film
from filmsApi.serializer import FilmSerializer


class CreateView(ListCreateAPIView):
    """

    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


    def get(self, request, *args, **kwargs):
        # response = urllib.request.urlopen('http://www.omdbapi.com/?i=tt0816692&plot=full')
        # print(response.read())
        return super().get(request, *args, **kwargs)

