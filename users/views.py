"""
    contains the views of user app
"""

from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm


# Create your views here.


def signup(request):
    """
    signup view takes the UserForm and renders it using users/signup.html template

    Parameters:
        request: contains information regarding request

    Returns:
        calls the render function using request object, template and context object
    """
    form = UserForm()
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "users/signup.html", context)


def index(request):
    """
    Index view
    """
    return HttpResponse("Hello, world. You're at the polls index.")
