from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse ("<h1>Las mejores hamburguesas del mundo<h1>")

