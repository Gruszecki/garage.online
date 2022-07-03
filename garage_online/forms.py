from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Band, Song, SocialLink, GlobalColorSet


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'contact_email', 'show_contact_email', 'short_desc', 'long_desc', 'genre', 'image', 'country', 'city', 'is_active', 'tags']


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'main_song', 'file', 'has_lyrics', 'language', 'lyrics']


class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields  = ['band_site', 'facebook', 'bandcamp', 'spotify', 'youtube', 'soundcloud', 'itunes', 'instagram']


class GlobalColorSetForm(forms.ModelForm):
    class Meta:
        model = GlobalColorSet
        fields = ['primary_color', 'text_color', 'background_color', 'user']
