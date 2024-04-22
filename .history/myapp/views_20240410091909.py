from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def hello(request):
    title  = 'Juegos que dan vida'
    return render(request, 'signup.html', {

        'mytitle': title
    })


    