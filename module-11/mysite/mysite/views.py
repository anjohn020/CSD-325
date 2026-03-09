from django.http import HttpResponse

def home(request):
    return HttpResponse("Johnson says Hello!")