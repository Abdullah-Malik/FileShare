"""
Module contains information regarding the forms that users app is using
"""

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import User


class ProfileCreationForm(UserCreationForm):
    """
    ProfileCreationForm extends the UserCreationForm of the Django
    and provides users with a form through which they can create their
    User model instance
    """

    class Meta:
        """
        Meta class
        """

        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "image",
        ]


class ProfileUpdateForm(ModelForm):
    """
    ProfileUpdateForm implements the ModelForm and provides a form
    using which an instance of User Model can be updated
    """

    class Meta:
        """
        Meta class
        """

        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "image",
        ]
