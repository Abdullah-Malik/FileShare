"""
contains the views of user app
"""

from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import UpdateView

from .forms import ProfileCreationForm, ProfileUpdateForm
from .models import User

# Create your views here.


def signup(request):
    """
    signup view takes the UserForm and renders it using users/signup.html template

    Parameters:
        request: contains information regarding request

    Returns:
        calls the render function using request object, template and context object
    """
    form = ProfileCreationForm()

    if request.method == "POST":
        form = ProfileCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "users/signup.html", context)


def index():
    """
    Index view
    """
    return HttpResponse("Hello, world. You're at the polls index.")


class ProfileUpdateView(UserPassesTestMixin, UpdateView):
    """
    ProfileUpdateView Extends Update View
    """

    model = User
    form_class = ProfileUpdateForm
    template_name = "users/profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    success_url = "/"

    def test_func(self):
        profile = self.get_object()
        if profile == self.request.user:
            return True
        return False
