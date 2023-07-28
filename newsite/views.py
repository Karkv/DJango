from django.shortcuts import HttpResponse, render


def index(request):
    return HttpResponse("Hello")


def home(request):
    a = 0
    b = 0
    result = 0
    if request.GET:
        # print("Posted")
        a=int(request.GET["n1"])
        b=int(request.GET["n2"])
        result=a+b

    return render(request, "hello.html", {"a": a, "b": b, "result": result})
