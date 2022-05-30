from django.shortcuts import render, redirect
from django.contrib.auth import login
from garage_online.forms import CustomUserCreationForm


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
