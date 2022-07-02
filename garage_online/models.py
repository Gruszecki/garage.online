from django.contrib.auth.models import User
from django.db import models
from garage_online import choices
from PIL import Image


# Create your models here.
class SocialLink(models.Model):
    band_site = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    bandcamp = models.CharField(max_length=100, null=True, blank=True)
    spotify = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)
    soundcloud = models.CharField(max_length=100, null=True, blank=True)
    itunes = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)


class Band(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    contact_email = models.EmailField(null=True, blank=True)
    show_contact_email = models.BooleanField(default=True)
    short_desc = models.TextField(max_length=150, null=False, blank=False)
    long_desc = models.TextField(null=False, blank=False)
    genre = models.PositiveSmallIntegerField(choices=choices.get_genres(), default=0)
    image = models.ImageField(upload_to='bands_photos', null=False, blank=False)
    country = models.CharField(max_length=2, choices=choices.get_countries(), default='PL')
    city = models.CharField(max_length=50, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    add_2db_date = models.DateField(auto_now_add=True)
    user = models.ManyToManyField(User, related_name='bands')
    social_links = models.OneToOneField(SocialLink, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        new_size = (760, int(760*img.height/img.width))
        img.thumbnail(new_size)
        img.save(self.image.path)


class Song(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    file = models.FileField(upload_to='songs', null=False, blank=False)
    has_lyrics = models.BooleanField(default=True)
    language = models.CharField(max_length=2, choices=choices.get_languages(), default='pl', null=True, blank=True)
    lyrics = models.TextField(null=True, blank=True)
    main_song = models.BooleanField(default=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.band} - {self.title}'


class GlobalColorSet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primary_color = models.CharField(max_length=7, null=False, blank=False, default='#fcba03')
    text_color = models.CharField(max_length=7, null=False, blank=False, default='#ffffff')
    background_color = models.CharField(max_length=7, null=False, blank=False, default='#000000')

