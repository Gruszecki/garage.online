import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from garage_online import forms, models


# Create your tests here.
@pytest.mark.django_db
def test_user_register_form_valid():
    # Arrange
    form = forms.CustomUserCreationForm({
        'username': 'WojciechGruszecki',
        'email': 'wojciech.gruszecki@gmail.com',
        'password1': 'Trudne#Hasło#692137420',
        'password2': 'Trudne#Hasło#692137420'
    })

    # Action
    result = form.is_valid()

    # Assert
    assert result


@pytest.mark.django_db
def test_user_register_form_invalid_username_not_unique():
    # Arrange
    User.objects.create(username='wojciech.gruszecki')

    form = forms.CustomUserCreationForm({
        'username': 'wojciech.gruszecki',
        'email': 'wojciech.gruszecki@gmail.com',
        'password1': 'Trudne#Hasło#692137420',
        'password2': 'Trudne#Hasło#692137420'
    })

    # Action
    result = form.is_valid()

    # Assert
    assert result is False
    assert form.errors['username'][0] == 'A user with that username already exists.'


@pytest.mark.django_db
def test_user_register_form_invalid_passwords_dont_match():
    # Arrange
    form = forms.CustomUserCreationForm({
        'username': 'wojciech.gruszecki',
        'email': 'wojciech.gruszecki@gmail.com',
        'password1': 'Trudne#Hasło#692137420',
        'password2': 'Trudne#Hasło#692137421'
    })

    # Action
    result = form.is_valid()

    # Assert
    assert result is False
    assert form.errors['password2'][0] == 'The two password fields didn’t match.'


# @pytest.mark.django_db
# def test_band_form_valid():
#     # Arrange
#     user = User.objects.create(username='wojciech.gruszecki')
#
#     band = forms.BandForm({
#         'name': 'Nazwa',
#         'contact_email': 'test@gmail.com',
#         'show_contact-email': True,
#         'short_desc': 'Short',
#         'long_desc': 'Long',
#         'genre': 0,
#         'image': 'image.jpg',
#         'country': 'PL',
#         'city': 'Kraków',
#         'is_active': True,
#         'tags': 'tag, another tag',
#         'user': user
#     })
#
#     # Action
#     result = band.is_valid()
#
#     # Assert
#     assert result
