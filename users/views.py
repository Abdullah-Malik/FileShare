from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def signup(request):
    form = UserForm()
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        
    context = {'form': form}
    return render(request, 'users/signup.html', context)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")