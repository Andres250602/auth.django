from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def hello(request):
    
    return render(request, 'signup.html', {
    'form': UserCreationForm
    })


    