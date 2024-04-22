from django.http import HttpResponse

def hello(request):
    """
    Retorna una respuesta HTTP con un mensaje centrado y estilizado que dice
    '¡Las mejores hamburguesas del mundo!', y algunos textos adicionales.
    """
    message = """
    <div style='font-family: Arial, sans-serif;
                text-align: center;
                background-color: #ffcccc; /* Color de fondo */
                padding: 20px; /* Espaciado interno */
                border-radius: 10px; /* Borde redondeado */'>
        <h1>¡Las mejores hamburguesas del mundo!</h1>
        <p style='font-family: "Helvetica Neue";'>Disfruta no solo hamburguesas, también nuestras malteadas</p>
        <p style='font-family: sans-serif;'>También nuestras chilli fries</p>
    </div>
    """
    return HttpResponse(message)



