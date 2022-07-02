from django.contrib import admin
from .models import Band, Song, SocialLink, GlobalColorSet

# Register your models here.
admin.site.register(Band)
admin.site.register(SocialLink)
admin.site.register(GlobalColorSet)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['band', 'title', 'has_lyrics', 'language']
    list_filter = ['band', 'has_lyrics', 'language']
    search_fields = ['band', 'lyrics']

