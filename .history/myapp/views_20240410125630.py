from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

def signup(request):
    if request.method== 'GET':
            return render(request, 'signup.html', {
    'form': UserCreationForm
    })
        
        
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
            return  render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'usuario ya existe'
            })  
            
            

        
        return  render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'contraseña no coincide'
                })
                

    
    return render(request, 'signup.html', {
    'form': UserCreationForm
    })
def home(request):
    return render (request, 'home.html')
def tasks(request):
    return render(request, 'tasks.html')

    