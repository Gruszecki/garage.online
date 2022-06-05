from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BandForm, SongForm, CustomUserCreationForm

from .models import Band, Song


# Create your views here.
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
            return redirect(new_song, band.id)


@login_required()
def edit_band(request, id):
    band = get_object_or_404(Band, pk=id)
    band_form = BandForm(request.POST or None, request.FILES or None, instance=band)

    if request.method == 'GET':
        return render(
            request,
            'garage_online/band.html',
            {
                'band_form': band_form,
                'band': band,
                'is_new': False
            }
        )
    elif request.method == 'POST':
        if band_form.is_valid():
            band_form.save()
        else:
            print('Editing band failed:', band_form.errors, sep='\n')
            return redirect(dashboard)
        if 'back_to_dashboard' in request.POST:
            return redirect(dashboard)
        elif 'go_to_songs' in request.POST:
            return redirect(new_song, band.id)


def lyrics_validation(form):
    if not form.has_lyrics:
        form.language = None
        form.lyrics = None

    return form


@login_required()
def new_song(request, id):
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
                return redirect(new_song, band.id)
            else:
                return redirect(dashboard)
        else:
            print('Adding new song failed:', form.errors, sep='\n')
            return redirect(dashboard)


@login_required()
def edit_songs(request, id):
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
                            return redirect(edit_songs, band.id)
            elif f'delete_{single_song.id}' in request.POST:
                single_song.delete()
                return redirect(edit_songs, band.id)

    return redirect(edit_songs, band.id)


def all_bands(request):
    bands = Band.objects.all()
    songs = Song.objects.all()
    return render(request, 'garage_online/all_bands.html', {'bands': bands, 'songs': songs})


def band_details(request, id):
    band = get_object_or_404(Band, pk=id)
    songs = Song.objects.filter(band=band)
    return render(request, 'garage_online/band_details.html', {'band': band, 'songs': songs})
