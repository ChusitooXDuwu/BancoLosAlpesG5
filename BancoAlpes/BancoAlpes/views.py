from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world! Django views")

#def fucntion that callls  pdf from folder docClientes
