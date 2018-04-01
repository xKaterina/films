from rest_framework import serializers

from filmsApi.models import Film


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'slogan', 'rated', 'released', 'runtime', 'genre', 'director', 'writer', 'actors',
                  'country', 'production', 'boxOffice')