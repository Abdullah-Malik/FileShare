from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from .models import FilesModel

# Create your views here.

def index(request):
    """
    Index view
    """
    return HttpResponse("Hello, world. You're at the home page.")

def dashboard(request):
    """
    Index view
    """
    return HttpResponse("Hello, world. You're at the dashboard.")

class FilesListView(ListView):
    model = FilesModel
    template_name = 'files/home.html'
    context_object_name = 'files'
    ordering = ['-date_posted']

class FileUploadView(CreateView):
    model = FilesModel
    fields = ['title', 'description', 'uploaded_file', 'thumbnail_image', 'date_posted']
    template_name = 'files/upload-file.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        print(form)
        form.save()
        return HttpResponseRedirect('files/home.html')

