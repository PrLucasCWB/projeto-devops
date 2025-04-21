from django.http import HttpResponse

def index(request):
    return HttpResponse("Alteração feita no projeto para PR!")
