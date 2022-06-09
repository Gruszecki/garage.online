from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BandForm, SongForm, CustomUserCreationForm, SocialLinkForm

from .models import Band, Song, SocialLink


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
            return redirect(dashboard)  # TODO: Add message success
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


def all_bands(request):
    bands = Band.objects.all()
    songs = Song.objects.all()
    return render(request, 'garage_online/all_bands.html', {'bands': bands, 'songs': songs})


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
                pass    # TODO: Dodać obługę wyjątków: message na górze ekranu, że się nie udało
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
                pass    # TODO: Nie można odebrać sobie prawd do zarządzania zespołem kiedy jest się jego jedynym zarządcą
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
                return redirect(user_settings)  # TODO: Nie można usunąć użytkownika kiedy jest jedynym zarządcą zespołu
    else:
        return redirect(dashboard)
