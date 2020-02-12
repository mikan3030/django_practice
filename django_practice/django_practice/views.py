from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html",
    {"title":"Hllo World"})

def hoge(request):
    if request.method == "POST":
        return HttpResponse("Hoge")
    elif request.method =="GET":
        return HttpResponse("hoge")
    else:
        return HttpResponse("Foo")

def fuga(request,foo):
    return render(request,"fuga.html",{'title': foo})