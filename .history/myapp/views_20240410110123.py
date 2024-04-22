from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method== 'GET':
        print('enviando formulario')
    else:
        print('obteniendo datos')

    
    return render(request, 'signup.html', {
    'form': UserCreationForm
    })
def home(request):
    return render (request, 'home.html')

    