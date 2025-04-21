from django.http import HttpResponse

def home(request):
    return HttpResponse("Alteração feita no projeto para PR!")
