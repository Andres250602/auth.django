from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    
    return render(request, 'signup.html', {
    'form': UserCreationForm
    })
def home(request):
    return render (request, 'home.html')

    