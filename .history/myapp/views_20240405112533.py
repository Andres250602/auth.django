from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse ("<h1 style='font-family: Arial, sans-serif; text-align: center;'>¡Las mejores hamburguesas del mundo!<h1>\n<pstyle='font-family:Helvetica Neue>Disfruta no solo hamburguesas, también nuestras malteadas<p> \n <p style='font-family:sans-serif> También nuestras chili fries<p>")



