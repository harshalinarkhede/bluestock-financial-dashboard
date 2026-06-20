from django.http import HttpResponse

def home(request):
    return HttpResponse("Bluestock Render Working")