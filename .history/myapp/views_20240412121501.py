from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TaskForm
from .models import tarea

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
    tasks = tarea.objects.filter(user=request.user, datecompleted__isnull=True )
    return render(request, 'tasks.html', {'tasks': tasks})
def signout(request):
    logout(request)
    return redirect ('home')
def signin(request):
    if request.method == 'GET':
        return render (request, 'signin.html',{
            'form': AuthenticationForm
        }) 
    else:   
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario y Contraseña incorrectos'
            })
        else:
            login (request, user)
            return redirect ('tasks')    
def create_task(request):
    if request.method == 'GET':
        return render (request, 'create_task.html', {
            'form':TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect ('tasks')
        except ValueError:
            return render (request, 'create_task.html', {
                'form':TaskForm,
                'error':'Por favor de ingresar datos validos'
                })
def task_details(request, task_id):
    print (task_id)
    return render(request, 'task_details.html')

    
    
    
    