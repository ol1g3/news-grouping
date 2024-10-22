from django.http import HttpResponse

def hello(request):
    return HttpResponse("HI! I am backend")