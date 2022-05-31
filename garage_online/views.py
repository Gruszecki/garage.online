from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BandForm

from .models import Band

from garage_online.forms import CustomUserCreationForm, BandForm


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
                'form': BandForm,
                'is_new': True
            }
        )
    elif request.method == 'POST':
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            band = form.save()
            request.user.bands.add(band)
            return redirect(dashboard)
        else:
            print('Adding new band failed:', form.errors, sep='\n')
            return redirect(dashboard)


@login_required()
def edit_band(request, name):
    band = get_object_or_404(Band, pk=Band.objects.get(name=name).id)
    band_form = BandForm(request.POST or None, request.FILES or None, instance=band)

    if request.method == 'POST':
        if band_form.is_valid():
            band_form.save()
            return redirect(dashboard)
        else:
            print('Editing band failed:', band_form.errors, sep='\n')
            return redirect(dashboard)
    elif request.method == 'GET':
        return render(
            request,
            'garage_online/band.html',
            {
                'form': band_form,
                'is_new': False
            }
        )


def all_bands(request):
    bands = Band.objects.all()
    return render(request, 'garage_online/all_bands.html', {'bands': bands})
