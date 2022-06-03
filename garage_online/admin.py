from django.contrib import admin
from .models import Band, Song

# Register your models here.
admin.site.register(Band)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['band', 'title', 'has_lyrics', 'language']
    list_filter = ['band', 'has_lyrics', 'language']
    search_fields = ['band', 'lyrics']

