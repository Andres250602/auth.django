from django.http import HttpResponse

def hello(request):
    """
    Retorna una respuesta HTTP con un mensaje centrado y estilizado que dice
    '¡Las mejores hamburguesas del mundo!', y algunos textos adicionales.
    """ 
    mensaje = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Afro Burger</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #ffcccc; 
                padding: 20px; 
            }
            .content {
            
                background-color: #fff; 
                padding: 20px; 
                border-radius: 10px; 
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); 
                width: 60%; 
                margin: 0 auto; 
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>¡Las mejores hamburguesas del mundo!</h1>
            <p>Disfruta no solo hamburguesas, también nuestras malteadas</p>
            <p>Y nuestras chilli fries</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(mensaje)
    