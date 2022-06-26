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
def test_user_register_form_invalid_email_already_in_db():
    # Arrange
    User.objects.create(email='wojciech.gruszecki@gmail.com')

    form = CustomUserCreationForm({
        'username': 'WojciechGruszecki',
        'email': 'wojciech.gruszecki@gmail.com',
        'password1': 'Trudne#Hasło#692137420',
        'password2': 'Trudne#Hasło#692137420'
    })

    # Action
    result = form.is_valid()

    # Assert
    assert result is False
    assert form.errors['email'][0] == 'Error email'
