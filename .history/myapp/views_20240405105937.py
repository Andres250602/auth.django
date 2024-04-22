from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse ("Las mejores hamburguesas del mundo")

