import os
import time
import datetime

from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO

from .models import Band, Song, SocialLink, GlobalColorSet


image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}


def parse_filters(request):
    split_filters = {
        'filterBands': [],
        'filterSongs': [],
        'filterGenres': [],
        'searchFields': [],
        'sortRadios': []
    }

    for name in request:
        try:
            group_id, filter_id = request[name].split('-')
            if group_id in list(split_filters):
                split_filters[group_id].append(filter_id)
        except ValueError:
            pass

    return split_filters


def use_filters(bands, split_filters):
    active = set()
    not_active = set()
    with_songs = set()
    without_songs = set()
    with_lyrics = set()
    without_lyrics = set()
    with_genres = set()

    # Band active/not active
    if 'active' in split_filters['filterBands'] and 'not_active' in split_filters['filterBands']:
        active = set(bands)
    elif 'active' in split_filters['filterBands'] or 'not_active' in split_filters['filterBands']:
        if 'active' in split_filters['filterBands']:
            active = set(bands.filter(is_active=True))
        elif 'not_active' in split_filters['filterBands']:
            not_active = set(bands.filter(is_active=False))
    else:
        active = set(bands)

    # Band with songs/without songs
    if 'with_songs' in split_filters['filterBands'] and 'without_songs' in split_filters['filterBands']:
        with_songs = set(bands)
    elif 'with_songs' in split_filters['filterBands'] or 'without_songs' in split_filters['filterBands']:
        if 'with_songs' in split_filters['filterBands']:
            for band in bands:
                if len(Song.objects.filter(band=band)) > 0:
                    with_songs.add(band)
        elif 'without_songs' in split_filters['filterBands']:
            for band in bands:
                if len(Song.objects.filter(band=band)) == 0:
                    without_songs.add(band)
    else:
        with_songs = set(bands)

    # Songs with lyrics/without lyrics
    if 'with_lyrics' in split_filters['filterSongs'] and 'without_lyrics' in split_filters['filterSongs'] and 'without_songs' not in split_filters['filterBands']:
        with_lyrics = set(bands)
    elif 'with_lyrics' in split_filters['filterSongs'] or 'without_lyrics' in split_filters['filterSongs']:
        if 'with_lyrics' in split_filters['filterSongs']:
            for band in bands:
                for song in Song.objects.filter(band=band):
                    if song.has_lyrics:
                        with_lyrics.add(band)
        elif 'without_lyrics' in split_filters['filterSongs']:
            for band in bands:
                for song in Song.objects.filter(band=band):
                    if not song.has_lyrics:
                        without_lyrics.add(band)
    elif 'with_lyrics' not in split_filters['filterSongs'] and 'without_lyrics' not in split_filters['filterSongs']:
        with_lyrics = set(bands)
    else:
        with_lyrics = set()

    # Bands' genres
    if len(split_filters['filterGenres']) > 0:
        for genre in split_filters['filterGenres']:
            for band in bands:
                if int(band.genre) == int(genre):
                    with_genres.add(band)
    else:
        with_genres = set(bands)

    filtered_bands = (active | not_active) & (with_songs | without_songs) & (with_lyrics | without_lyrics) & with_genres

    return filtered_bands


def use_searching(bands, split_filters, phrase):
    bands = set(bands)
    searched_bands = set()

    if len(split_filters['searchFields']) == 0:
        split_filters['searchFields'] = ['name', 'desc', 'song', 'tag', 'city']

    for band in bands:
        if 'name' in split_filters['searchFields']:
            if phrase in band.name.lower():
                searched_bands.add(band)
        if 'desc' in split_filters['searchFields']:
            if phrase in band.short_desc.lower() or phrase in band.long_desc.lower():
                searched_bands.add(band)
        if 'song' in split_filters['searchFields']:
            songs = Song.objects.filter(band=band)
            for song in songs:
                if phrase in song.title.lower():
                    searched_bands.add(band)
        if 'tag' in split_filters['searchFields']:
            if band.tags:
                if phrase in band.tags.lower():
                    searched_bands.add(band)
        if 'city' in split_filters['searchFields']:
            if phrase in band.city.lower():
                searched_bands.add(band)

    return searched_bands


def use_sorting(bands, split_filters):
    sorted_bands = []

    if len(split_filters['sortRadios']) == 0:
        sorted_bands = sorted(bands, key=lambda band: time.mktime(datetime.datetime.strptime(str(band.add_2db_date), "%Y-%m-%d").timetuple()), reverse=True)
    elif split_filters['sortRadios'][0] == 'newest':
        sorted_bands = sorted(bands, key=lambda band: time.mktime(datetime.datetime.strptime(str(band.add_2db_date), "%Y-%m-%d").timetuple()), reverse=True)
    elif split_filters['sortRadios'][0] == 'oldest':
        sorted_bands = sorted(bands, key=lambda band: time.mktime(datetime.datetime.strptime(str(band.add_2db_date), "%Y-%m-%d").timetuple()))
    elif split_filters['sortRadios'][0] == 'a_z':
        sorted_bands = sorted(bands, key=lambda band: band.name.lower())
    elif split_filters['sortRadios'][0] == 'z_a':
        sorted_bands = sorted(bands, key=lambda band: band.name.lower(), reverse=True)

    return sorted_bands


def use_combined_filters(bands, split_filters, phrase):
    filtered_bands = use_filters(bands, split_filters)
    searched_bands = use_searching(filtered_bands, split_filters, phrase) if len(phrase) else filtered_bands
    sorted_bands = use_sorting(searched_bands, split_filters)

    return sorted_bands


def lyrics_validation(form):
    if not form.has_lyrics:
        form.language = None
        form.lyrics = None

    return form

