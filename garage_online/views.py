from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404

from .choices import get_filters
from .forms import BandForm, SongForm, CustomUserCreationForm, SocialLinkForm
from .models import Band, Song, SocialLink

import time
import datetime


# Create your views here.
@login_required()
def dashboard(request):
    bands = Band.objects.filter(user=request.user) if request.user.is_authenticated else None
    return render(request, 'garage_online/dashboard.html', {'bands': bands})


def register(request):
    if request.method == 'GET':
        return render(
            request,
            'garage_online/register.html',
            {'form': CustomUserCreationForm}
        )
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(dashboard)


@login_required()
def new_band(request):
    if request.method == 'GET':
        return render(
            request,
            'garage_online/band.html',
            {
                'band_form': BandForm,
                'is_new': True
            }
        )
    elif request.method == 'POST':
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            band = form.save()
            request.user.bands.add(band)
        else:
            print('Adding new band failed:', form.errors, sep='\n')
            return redirect(dashboard)

        if 'back_to_dashboard' in request.POST:
            return redirect(dashboard)
        elif 'go_to_songs' in request.POST:
            return redirect(new_song, band.id, band.name)


@login_required()
def edit_band(request, id, name):
    band = get_object_or_404(Band, pk=id)
    socials = SocialLink.objects.filter(band=band)
    band_form = BandForm(request.POST or None, request.FILES or None, instance=band)
    users_with_privileges = User.objects.filter(bands=band)

    if request.method == 'GET':
        return render(
            request,
            'garage_online/band.html',
            {
                'users_with_privileges': users_with_privileges,
                'band_form': band_form,
                'social_form': SocialLinkForm,
                'band': band,
                'socials': socials,
                'is_new': False
            }
        )
    elif request.method == 'POST':
        # Save and go to dashboard without adding songs
        if band_form.is_valid() and 'back_to_dashboard' in request.POST:
            band_form.save()
            return redirect(dashboard)
        # Save and add songs
        elif band_form.is_valid() and 'go_to_songs' in request.POST:
            band_form.save()
            return redirect(new_song, band.id, band.name)
        # Delete band
        elif 'delete_band' in request.POST:
            band.delete()
            return redirect(dashboard)
        # Social links
        elif 'add_social_links' in request.POST:
            social_form = SocialLinkForm(request.POST)
            if social_form.is_valid():
                social = social_form.save(commit=False)
                social.band = band
                social.save()
            return redirect(edit_band, band.id, band.name)
        # Remove link
        elif 'remove_link' in request.POST:
            link_id = request.POST.get('remove_link')
            link = SocialLink.objects.get(id=link_id)
            link.delete()
            return redirect(edit_band, band.id, band.name)
        # Error
        else:
            print('Editing band failed:', band_form.errors)
            return redirect(dashboard)


def band_details(request, id, name):
    band = get_object_or_404(Band, pk=id)
    songs = Song.objects.filter(band=band)
    links = SocialLink.objects.filter(band=band)
    return render(request, 'garage_online/band_details.html', {'band': band, 'songs': songs, 'links': links})


def parse_filters(request):
    split_filters = {
        'filterBands': [],
        'filterSongs': [],
        'filterGenres': [],
        'searchFields': [],
        'sortRadios': []
    }

    for name in request:
        print(request[name], name)
        try:
            group_id, filter_id = request[name].split('-')
            if group_id in list(split_filters):
                split_filters[group_id].append(filter_id)
        except ValueError:
            pass

    return split_filters


def use_filters(bands, split_filters):
    print(split_filters)
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
            if phrase in band.tags.lower():
                searched_bands.add(band)
        if 'city' in split_filters['searchFields']:
            if phrase in band.city.lower():
                searched_bands.add(band)

    return searched_bands


def use_sorting(bands, split_filters):
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


def all_bands(request):
    bands = Band.objects.all()
    songs = Song.objects.all()
    filters = get_filters()
    split_filters = parse_filters(request.POST)

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        if 'set_filters' in request.POST:
            phrase = request.POST['search-place-canvas'].lower()
            bands = use_combined_filters(bands, split_filters, phrase)
        elif 'btn-search' in request.POST:
            phrase = request.POST['search-place'].lower()
            bands = use_searching(bands, split_filters, phrase) if len(phrase) else bands

    return render(request, 'garage_online/all_bands.html', {'bands': use_sorting(bands, split_filters), 'songs': songs, 'filters': filters})


@login_required()
def user_bands(request):
    bands = Band.objects.filter(user=request.user)
    band_songs = {}
    band_forms = {}
    song_forms = {}
    social_links = {}
    users_with_privileges = {}

    for band in bands:
        band_forms[band.id] = BandForm(request.POST or None, request.FILES or None, instance=band)

        songs = Song.objects.filter(band=band)
        song_forms_dict = {}

        for song in songs:
            song_forms_dict[song.id] = SongForm(request.POST or None, request.FILES or None, instance=song)
        if len(song_forms_dict) < 3:
            song_forms_dict[0] = SongForm(request.POST or None, request.FILES or None)

        song_forms[band.id] = song_forms_dict
        band_songs[band.id] = songs

        try:
            links_obj = SocialLink.objects.get(band=band)
        except SocialLink.DoesNotExist:
            links_obj = None

        social_links[band.id] = SocialLinkForm(request.POST or None, instance=links_obj)
        users_with_privileges[band] = band.user.all()

    new_band_form = BandForm(request.POST or None, request.FILES or None)

    if request.method == 'GET':
        return render(
            request,
            'garage_online/user_bands.html',
            {
                'bands': bands,
                'band_forms': band_forms,
                'new_band_form': new_band_form,
                'band_songs': band_songs,
                'song_forms': song_forms,
                'social_links': social_links,
                'users_with_privileges': users_with_privileges
            }
        )
    elif request.method == 'POST':
        if 'save_band' in request.POST:
            band_id = int(request.POST.get('band_id'))
            if band_forms[band_id].is_valid():
                band_forms[band_id].save()
            else:
                messages.success(request, f'Nie udało się zapisać zespołu.', fail_silently=True)
                print('Nie udało się zapisać zespołu.')
                print(band_forms[band_id].errors)

            return redirect(user_bands)
        elif 'new_band' in request.POST:
            if new_band_form.is_valid():
                band = new_band_form.save()
                request.user.bands.add(band)
            else:
                messages.success(request, f'Nie udało się zapisać zespołu.', fail_silently=True)
                print('Nie udało się zapisać zespołu.')
                print(new_band_form.errors)

            return redirect(user_bands)
        elif 'save_songs' in request.POST:
            band_id = int(request.POST.get('band_id'))
            song_id = int(request.POST.get('song_id'))

            band = Band.objects.get(id=band_id)
            song_form = song_forms[band_id][song_id]
            if song_form.is_valid():
                form = song_form.save(commit=False)
                form = lyrics_validation(form)
                form.band = band
                form.save()
                messages.success(request, f'Utwór {form.title} został pomyślnie zapisany.', fail_silently=True)
            else:
                print('Nie udało się zapisać utworu.')       # Dodać komunikat form not valid
                print(song_form.errors)

            return redirect(user_bands)
        elif 'save_links' in request.POST:
            band_id = int(request.POST.get('band_id'))
            social_link_form = social_links[band_id]
            band = Band.objects.get(id=band_id)

            if social_link_form.is_valid():
                socials = social_link_form.save()
                band.social_links = socials
                band.save()
                messages.success(request, f'Linki zespołu {band.name} zostały zauktualizowane.', fail_silently=True)
                return redirect(user_bands)
        elif 'give_privileges' in request.POST:
            band_id = int(request.POST.get('band_id'))
            band = Band.objects.get(id=band_id)
            email = request.POST.get('user_email')
            try:
                additional_user = User.objects.get(email=email)
                band.user.add(additional_user)
                messages.success(request, f'Pomyślnie nadano uprawnienia dla użytkownika o podanym adresise e-mail: {email}.', fail_silently=True)
            except ObjectDoesNotExist:
                messages.success(request, f'Nadanie uprawnień nie powiodło się. Nie znaleziono użytkownika o podanym adresise e-mail: {email}.', fail_silently=True)
            finally:
                return redirect(user_bands)
        elif 'take_privileges' in request.POST:
            band_id = int(request.POST.get('band_id'))
            band = Band.objects.get(id=band_id)
            selected_user = request.POST.get('users_to_privilege_take', False)
            if len(users_with_privileges[band]) > 1:
                if selected_user:
                    user = User.objects.get(email=selected_user)
                    band.user.remove(user)
                    messages.success(request, f'Pomyślnie odebrano uprawnienia.', fail_silently=True)
                    return redirect(user_bands)
            else:
                messages.success(request, f'Nie możesz odebrać uprawnień do zespołu, którego jesteś jedynym zarządcą.', fail_silently=True)

            return redirect(user_bands)
        else:
            for band in bands:
                if f'delete-band-{band.id}' in request.POST:
                    band.delete()
                    messages.success(request, f'Zespół {band.name} został usunięty.', fail_silently=True)
                    return redirect(user_bands)
                songs = Song.objects.filter(band=band)
                for song in songs:
                    if f'delete-song-{band.id}-{song.id}' in request.POST:
                        song.delete()
                        messages.success(request, f'Utwór {song.title} został usunięty.', fail_silently=True)
                        return redirect(user_bands)

            print('Editing band failed.')
            print(request.POST)
            return redirect(user_bands)


def lyrics_validation(form):
    if not form.has_lyrics:
        form.language = None
        form.lyrics = None

    return form


@login_required()
def new_song(request, id, name):
    band = Band.objects.get(id=id)

    if request.method == 'GET':
        return render(
            request,
            'garage_online/song.html',
            {
                'song_form': SongForm,
                'band': band,
                'number_of_songs_already_in_database': len(Song.objects.filter(band=band))
            }
        )
    elif request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song_form = form.save(commit=False)
            song_form = lyrics_validation(song_form)
            song_form.band = band
            song_form.save()

            if len(Song.objects.filter(band=band)) < 3:
                return redirect(new_song, band.id, band.name)
            else:
                return redirect(dashboard)
        else:
            print('Adding new song failed:', form.errors, sep='\n')
            return redirect(dashboard)


@login_required()
def edit_songs(request, id, name):
    band = Band.objects.get(id=id)
    songs = Song.objects.filter(band=band)

    songs_forms = []
    for single_song in songs:
        songs_forms.append([SongForm(request.POST or None, request.FILES or None, instance=single_song), single_song.id])

    if request.method == 'GET':
        return render(
            request,
            'garage_online/edit_songs.html',
            {
                'songs': songs,
                'songs_forms': songs_forms,
                'band': band,
                'is_new': False
            }
        )
    elif request.method == 'POST':
        for single_song in songs:
            if f'save_{single_song.id}' in request.POST:
                for form in songs_forms:
                    if form[1] == single_song.id:
                        if form[0].is_valid():
                            song_form = form[0].save(commit=False)
                            song_form = lyrics_validation(song_form)
                            song_form.band = band
                            song_form.save()
                            return redirect(edit_songs, band.id, band.name)
            elif f'delete_{single_song.id}' in request.POST:
                single_song.delete()
                return redirect(edit_songs, band.id, band.name)

    return redirect(edit_songs, band.id, band.name)


@login_required()
def manage_privileges(request, id, name):
    band = Band.objects.get(id=id)
    users_with_privileges = band.user.all()

    if request.method == 'GET':
        return render(
            request,
            'garage_online/manage_privileges.html',
            {
                'band': band,
                'users_with_privileges': users_with_privileges
            }
        )
    elif request.method == 'POST':
        if 'give_privileges' in request.POST:
            email = request.POST.get('user_email')
            try:
                additional_user = User.objects.get(email=email)
                band.user.add(additional_user)
            except ObjectDoesNotExist:
                messages.success(request, f'Nadanie uprawnień nie powiodło się. Nie znaleziono użytkownika o podanym adresise e-mail: {email}', fail_silently=True)
            finally:
                return redirect(manage_privileges, band.id, band.name)
        elif 'take_privileges' in request.POST:
            selected_user = request.POST.get('users_to_privilege_take', False)
            if len(users_with_privileges) > 1:
                if selected_user:
                    user = User.objects.get(email=selected_user)
                    band.user.remove(user)
                return redirect(dashboard)
            else:
                pass
                return redirect(manage_privileges, band.id, band.name)

        return redirect(manage_privileges, band.id, band.name)     # In case of problems


@login_required()
def user_settings(request):
    if request.method == 'GET':
        return render(
            request,
            'garage_online/user_settings.html'
        )
    elif request.method == 'POST' and 'delete_user' in request.POST:
        all_bands_of_user = Band.objects.filter(user=request.user)
        for band in all_bands_of_user:
            if len(band.user.all()) > 1:
                request.user.delete()
                return redirect(all_bands)
            else:
                return redirect(user_settings)
    else:
        return redirect(dashboard)


