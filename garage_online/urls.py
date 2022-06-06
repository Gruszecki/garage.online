"""garage_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# garage_online/urls.py

from django.urls import path
from garage_online import views
from django.conf.urls import include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('all/', views.all_bands, name='all_bands'),
    path('band/new', views.new_band, name='new_band'),
    path('band/<int:id>', views.band_details, name='band_details'),
    path('band/<int:id>/edit', views.edit_band, name='edit_band'),
    path('band/<int:id>/add_song', views.new_song, name='add_song'),
    path('band/<int:id>/edit_songs', views.edit_songs, name='edit_songs'),
    path('band/<int:id>/manage_privileges', views.manage_privileges, name='manage_privileges')
]
