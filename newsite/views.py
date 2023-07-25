from django.shortcuts import HttpResponse,render

def index(request):
    return HttpResponse( "Hello")
def home(request):
    return render(request,"hello.html")