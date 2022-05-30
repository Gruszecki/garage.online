from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import Band


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class BandCreationForm(ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'short_desc', 'long_desc', 'genre', 'image', 'country', 'city', 'is_active', 'tags']
