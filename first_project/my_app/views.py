from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Home Page!")

def about(request):
    return HttpResponse("This is the About Page.")

def contact(request):
    return HttpResponse("This is the Contact Page.")

def service(request):
    return HttpResponse("This is the Service Page.")