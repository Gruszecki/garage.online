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
            return redirect(song, band.id)


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
            return redirect(song, band.id)


@login_required()
def song(request, id):
    if request.method == 'GET':
        return render(
            request,
            'garage_online/song.html',
            {
                'song_form': SongForm
            }
        )
    elif request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        band = Band.objects.get(id=id)
        if form.is_valid():
            song_form = form.save(commit=False)

            if not song_form.has_lyrics:
                song_form.language = None

            song_form.band = band
            song_form.save()
            return redirect(song, band.id)
        else:
            print('Adding new song failed:', form.errors, sep='\n')
            return redirect(dashboard)


def all_bands(request):
    bands = Band.objects.all()
    songs = Song.objects.all()
    return render(request, 'garage_online/all_bands.html', {'bands': bands, 'songs': songs})


def band_details(request, id):
    band = get_object_or_404(Band, pk=id)
    songs = Song.objects.filter(band=band)
    return render(request, 'garage_online/band_details.html', {'band': band, 'songs': songs})
