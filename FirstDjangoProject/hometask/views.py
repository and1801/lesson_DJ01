from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    return render(request, 'hometask/index.html', {'caption':"TocaBoca"})

def new(request):
    return render(request, 'hometask/new.html')

def about(request):
    return render(request, 'hometask/about.html')

def services(request):
    return render(request, 'hometask/services.html')

def contact(request):
    return render(request, 'hometask/contact.html')