from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def foo(request):
    return HttpResponse("Foo")

def woo(request):
    return HttpResponse("Woo")