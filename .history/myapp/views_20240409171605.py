from django.http import HttpResponse
import mensaje.html

def hello(request):
   
    Retorna una respuesta HTTP con un mensaje centrado y estilizado que dice
   
    return HttpResponse(mensaje)

def about(request):
    return HttpResponse('About')

    