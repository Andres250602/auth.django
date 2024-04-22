from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

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
                return HttpResponse('usuario creado con exito')
            except:
                return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Usuario ya existe'
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

    