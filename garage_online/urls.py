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

from django.conf.urls import include
from django.urls import path, re_path
from garage_online import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('', views.all_bands, name='all_bands'),
    path('band/<int:id>/<str:name>', views.band_details, name='band_details'),
    path('user/bands', views.user_bands, name='user_bands'),
    path('settings', views.user_settings, name='user_settings'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
