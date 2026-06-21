from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>Bluestock Dashboard LIVE ✔</h1>
    <p>Submission Ready Version</p>
    """)