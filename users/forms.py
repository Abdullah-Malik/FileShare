"""
Module contains information regarding the forms that users app is using
"""

from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import ModelForm

from .models import User


class UserForm(UserCreationForm):
    """
    UserForm extends the UserCreationForm of the Django users model
    """

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "image",
        ]
