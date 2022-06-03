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
            return redirect(songs, band.name)


@login_required()
def edit_band(request, name):
    band = get_object_or_404(Band, pk=Band.objects.get(name=name).id)
    band_form = BandForm(request.POST or None, request.FILES or None, instance=band)

    if request.method == 'GET':
        return render(
            request,
            'garage_online/band.html',
            {
                'band_form': band_form,
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
            return redirect(songs, band.name)


@login_required()
def songs(request, name):
    if request.method == 'GET':
        return render(
            request,
            'garage_online/songs.html',
            {
                'songs_form': SongForm
            }
        )
    elif request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        band = Band.objects.get(name=name)
        if form.is_valid():
            song = form.save(commit=False)
            song.band = band
            song.save()
            return redirect(songs, band.name)
        else:
            print('Adding new band failed:', form.errors, sep='\n')
            return redirect(dashboard)




def all_bands(request):
    bands = Band.objects.all()
    return render(request, 'garage_online/all_bands.html', {'bands': bands})


def band_details(request, name):
    band = get_object_or_404(Band, pk=Band.objects.get(name=name).id)
    return render(request, 'garage_online/band_details.html', {'band': band})
