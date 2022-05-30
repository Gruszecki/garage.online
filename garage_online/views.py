from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from garage_online.forms import CustomUserCreationForm, BandCreationForm


# Create your views here.
def dashboard(request):
    return render(request, 'garage_online/dashboard.html')


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
            'garage_online/new_band.html',
            {'form': BandCreationForm}
        )
    elif request.method == 'POST':
        form = BandCreationForm(request.POST)
        if form.is_valid():
            band = form.save()
            request.user.bands.add(band)
            return redirect(dashboard)
        else:
            print('Adding new band failed:', form.errors, sep='\n')
            return redirect(dashboard)
