from django.http import HttpResponse

def hello(request):
    """
    Retorna una respuesta HTTP con un mensaje centrado y estilizado que dice
    '¡Las mejores hamburguesas del mundo!', y algunos textos adicionales.
    """
    message = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Las mejores hamburguesas del mundo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #ffcccc; /* Color de fondo */
                padding: 20px; /* Espaciado interno */
            }
            .content {
                background-color: #fff; /* Color de fondo del contenido */
                padding: 20px; /* Espaciado interno del contenido */
                border-radius: 10px; /* Borde redondeado */
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Sombra */
                width: 60%; /* Ancho del contenedor */
                margin: 0 auto; /* Centrado horizontal */
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>¡Las mejores hamburguesas del mundo!</h1>
            <p>Disfruta no solo hamburguesas, también nuestras malteadas</p>
            <p>También nuestras chilli fries</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(message)
