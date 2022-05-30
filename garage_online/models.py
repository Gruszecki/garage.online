from django.db import models
from garage_online import choices
from django.contrib.auth.models import User


# Create your models here.
class Band(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    short_desc = models.TextField(max_length=150, null=False, blank=False)
    long_desc = models.TextField(null=False, blank=False)
    genre = models.PositiveSmallIntegerField(choices=choices.get_genres(), default=0)
    image = models.ImageField(upload_to='bands_photos', null=True, blank=True)
    country = models.CharField(max_length=2, choices=choices.get_countries(), default='PL')
    city = models.CharField(max_length=50, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    user = models.ManyToManyField(User, related_name='bands')

    def __str__(self):
        return self.name
