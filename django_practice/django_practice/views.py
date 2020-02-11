from django.http import Httpresponse

def index(request):
    return Httpresponse("Hello World")