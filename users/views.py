from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import User

# Create your views here.

def index(request):
    #return HttpResponse("Login Page")
    
    #property = get_object_or_404(Property, pk=property_id)
    
    args = {}
    return HttpResponse('<h1>Log in page</h1>')


    #return redirect('properties.views.listing', args)
