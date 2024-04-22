from django.shortcuts import render
from django.http import HttpResponse


def hello(request):

    return HttpResponse('Las mejores hamburguesas del mundo')

def about(request):
    return HttpResponse('About')

    