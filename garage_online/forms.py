from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import Band, Song


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class BandForm(ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'short_desc', 'long_desc', 'genre', 'image', 'country', 'city', 'is_active', 'tags']


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'file', 'has_lyrics', 'language', 'lyrics']
