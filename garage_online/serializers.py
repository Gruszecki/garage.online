from rest_framework import serializers
from .models import Band, Song


class BandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Band
        fields = ['name', 'short_desc', 'long_desc', 'genre', 'country', 'city', 'is_active', 'tags']


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'has_lyrics', 'language', 'lyrics', 'band']
