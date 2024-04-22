from django.http import HttpResponse

def hello(request):
    message = """
    <div style='font-family: Arial, sans-serif;
                text-align: center;
                background-color: #ffcccc; 
                padding: 25px; 
                border-radius: 5px; 
        <h1>¡Las mejores hamburguesas del mundo!</h1>
        <p style='font-family: "Helvetica Neue";'>Disfruta no solo hamburguesas, también nuestras malteadas</p>
        <p style='font-family: sans-serif;'>y También nuestras chilli fries</p>
    </div>
    """
    return HttpResponse(message)



