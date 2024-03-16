from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello world! Django views")

def healthCheck(request):
    return HttpResponse("ok")

#def fucntion that callls  pdf from folder docClientes
