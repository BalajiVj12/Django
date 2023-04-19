from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    msg = "<h1>Hi! hello</h1>"
    return HttpResponse(msg)

def house(request):
    message ="<p>Hi. How are you?</p>"
    return HttpResponse(message)
    
def current_datetime(request):
    now = datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now  
    # // we can use %s or %now
    return HttpResponse(html)

def temp(request):
    return render(request,"index.html")
