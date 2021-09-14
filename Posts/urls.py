"""
defines all the urls that Posts app is using
"""
from django.urls import path

from .views import (
    PostDashboardView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    PostUploadView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="Posts-home"),
    path(
        "dashboard/",
        PostDashboardView.as_view(),
        name="Posts-dashboard",
    ),
    path("file/<int:pk>/", PostDetailView.as_view(), name="Posts-detail"),
    path(
        "file/<int:pk>/update/",
        PostUpdateView.as_view(),
        name="Posts-update",
    ),
    path(
        "file/<int:pk>/delete/",
        PostDeleteView.as_view(),
        name="Posts-delete",
    ),
    path("file/new/", PostUploadView.as_view(), name="Posts-create"),
]
