"""
contains all the urls that users app is using
"""

from django.urls import path

from . import views
from .views import ProfileUpdateView

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("profile/<str:username>/", ProfileUpdateView.as_view(), name="profile"),
]
