from django.db.models import fields
from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email' ,'password1','password2', 'image',]