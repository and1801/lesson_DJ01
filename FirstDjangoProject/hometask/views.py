from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def data(request):
    return HttpResponse("<h1>Здесь data</h1>")

def test(request):
    return HttpResponse("<h1>Здесь test</h1>")