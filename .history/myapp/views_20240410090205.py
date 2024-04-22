from django.shortcuts import render
from django.http import HttpResponse


def hello(request):

    return HttpResponse()

def about(request):
    return HttpResponse('About')

    