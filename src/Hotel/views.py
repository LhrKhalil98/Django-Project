from django.shortcuts import render, get_object_or_404
from django.urls import reverse 


def home (request) : 
    return render (request , "home.html" )
def galeries (request ) : 
    return render (request , "Galeries.html" )
def services (request) : 
    return render (request , "services.html" , {})
def rooms (request) : 
    return render (request , "rooms.html" , {})