from django.http import HttpResponse

def hello(request):
    """
    '¡Las mejores hamburguesas del mundo!', y algunos textos adicionales.
    """
    message = """
    <div style='font-family: Arial, sans-serif;
                text-align: center;
                background-color: #ffcccc; 
                padding: 20px; 
                border-radius: 10px; 
        <h1>¡Las mejores hamburguesas del mundo!</h1>
        <p style='font-family: "Helvetica Neue";'>Disfruta no solo hamburguesas, también nuestras malteadas</p>
        <p style='font-family: sans-serif;'>También nuestras chilli fries</p>
    </div>
    """
    return HttpResponse(message)



