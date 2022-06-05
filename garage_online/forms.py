from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Band, Song


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'short_desc', 'long_desc', 'genre', 'image', 'country', 'city', 'is_active', 'tags']


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'file', 'has_lyrics', 'language', 'lyrics']


class AdditionalUserForm(forms.Form):
    email = forms.EmailField()
