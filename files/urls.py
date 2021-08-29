from django.urls import path
from django.urls.resolvers import URLPattern
from .views import FileUploadView, FilesListView

from . import views

urlpatterns = [
    path("", FilesListView.as_view(), name="files-home"),
    path("dashboard/", views.dashboard, name="files-dashboard"),
    path("upload-file/", FileUploadView.as_view(), name="upload-file"),
]