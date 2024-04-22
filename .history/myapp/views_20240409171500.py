from django.http import HttpResponse

def hello(request):
    """
    Retorna una respuesta HTTP con un mensaje centrado y estilizado que dice
    '¡Las mejores hamburguesas del mundo!', y algunos textos adicionales.
    """ 
    mensaje = """
   
    """
    return HttpResponse(mensaje)

def about(request):
    return HttpResponse('About')

    