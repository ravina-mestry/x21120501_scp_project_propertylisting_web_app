from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request):
    
    args = {}
    #return HttpResponse("<h1>Hello</h1>")
    return render(request,'landing_page.html',args)