"""
    contains all the urls that users app is using
"""

from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path("signup/", views.signup, name="users-signup"),
]
