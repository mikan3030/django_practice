from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Page
from .models import Feed
from .forms import FeedForm

def index(request):
    feeds = Feed.objects.all()
    return render(request,"index.html",
    {"title":"Hllo World","l":["ok","kusa","nashi"]
    ,"feeds":feeds})

def hoge(request):
    if request.method == "POST":
        return HttpResponse("Hoge")
    elif request.method =="GET":
        return HttpResponse("hoge")
    else:
        return HttpResponse("Foo")

def fuga(request,foo):
    return render(request,"fuga.html",{'title': foo})

def search(request):
    q = request.GET.get("q")
    return HttpResponse(q)

def render_form(request):
    return render(request,"login.html")

def login(request):
    if (request.POST["username"] and request.POST["email"]):
        return render(request,"check.html",{"email":request.POST["email"],"username":request.POST["username"]})
    else:
        return render(request,"error.html")

def upload(request):
    if (request.method=="POST" 
        and request.FILES
        and request.FILES["image"]):
        binary = request.FILES["image"]
        image = open("static/hoge.png","wb")
        for chunk in binary.chunks():
            image.write(chunk)
        return render(request,"result.html")
    else:
        # return HttpResponseRedirect("/form")
        return render(request,"form.html")

def form(request):
    form = FeedForm()
    return render(request,"form.html"
    ,{"form":form})

def post(request):
    if request.method != "POST":
        return redirect(to="/form")
    form = FeedForm(request.POST)
    if (form.is_valid()):
        feed = Feed.objects.create(
            title = request.POST["title"],
            href = request.POST["href"],
            description = request.POST["description"]
        )
        feed.save()
        return redirect(to="/")
    else:
        return redirect(to="/form")

def search(request):
    try:
        feed = Feed.objects.get(title=request.GET["q"])
        return render(request,"result.html",
        {"feeds":[feed]})
    except:
        return render(request,"result.html",
        {"feeds":[]})

def change_title(request):
    feed = Feed.objects.get(id=request.POST["id"])
    # feed.title = request.POST["title"]
    feed.title = kusa
    feed.save()
    return render(request,"result.html",
    {"feed":[feed]})

def delete(request):
    if (request.method == "POST" 
    and request.POST["id"]):
        feed = Feed.objects.get(id=request.POST["id"])
        feed.delete()
        return redirect(to="/")