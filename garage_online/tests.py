import pytest
from django.test import TestCase
from garage_online.forms import CustomUserCreationForm
from django.contrib.auth.models import User


# Create your tests here.
@pytest.mark.django_db
def test_user_register_form_valid():
    # Arrange
    form = CustomUserCreationForm({
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

    form = CustomUserCreationForm({
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
    form = CustomUserCreationForm({
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


