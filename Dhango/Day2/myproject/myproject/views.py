from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("<h1>welcome to django world</h1>")
