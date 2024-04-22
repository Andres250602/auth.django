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
        if request.POST['password1'] == request.POST['password1']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                User.save()
                return HttpResponse('usuario creado con exito')
            except:
                return HttpResponse('usuario ya existe')
            

            #user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            #User.save()
            #return HttpResponse('usuario creado con exito')
    return HttpResponse('password no coincide')         

 

    
    #return render(request, 'signup.html', {
   # 'form': UserCreationForm
    #})
#def home(request):
    #return render (request, 'home.html')

    