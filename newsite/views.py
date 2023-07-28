from audioop import add
from django.shortcuts import HttpResponse, render


def index(request):
    return HttpResponse("Hello")


def home(request):
    a = 0
    b = 0
    result = 0
    if request.GET:
        # print("Posted")
        a = int(request.GET["n1"])
        b = int(request.GET["n2"])
        result = a + b

    return render(request, "hello.html", {"a": a, "b": b, "result": result})
def sub(request):
    n=0
    m=0
    result=0

    if request.GET:
        # print("Posted")
        n=int(request.GET["n1"])
        m=int(request.GET["n2"])
        result=n-m
    return render(request,"subtract.html",{"n":n , "m":m,"result":result})
    


def cal(request):
    a=0
    b=0
    result=0

    if request.GET:
        a=int(request.GET["n1"])
        b=int(request.GET["n2"])
        cmd=request.GET["option"]
        if cmd=="add":

            result=a+b
        elif cmd=="sub":
            result=a-b
        
        elif cmd=="mul":
            result=a*b

        elif cmd=="div":
            result=a/b        
    
    return render(request,"calculator1.html",{"a":a,"b":b,"result":result})


def newcal(request):
    a=0
    b=0
    result=0
    if request.GET:
        a=int(request.GET["n1"])
        b=int(request.GET["n2"])
        cmd=request.GET["option"]

        if cmd=="add":
            result=a+b
        elif cmd=="sub":
            result=a-b
        elif cmd=="mul":
            result=a*b
        elif cmd=="div":
            result=a/b
    return render(request,"newcal.html",{"a":a,"b":b,"result":result})

def list(request):
    a=0
    b=0
    result=0

    if request.GET:
        a=int(request.GET["n1"])
        b=int(request.GET["n2"])

        cmd=request.GET("operation")

        if cmd=="add":
            result=a+b

        elif cmd=="sub":
            result=a+b

        
    return render(request,"listcalculator.html",{"a":a,"b":b,"result":result})