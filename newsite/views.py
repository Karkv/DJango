from audioop import add
from django.shortcuts import HttpResponse, render


def index(request):
    
    return HttpResponse("Hello")
def resultview(request):
    results={1:{"name":"Popat","physics":80,"chemistry":78,"maths":75},2:{"name":"Bhide","physics":88,"chemistry":77,"maths":55}}
    rollno=0
    result=""
    if request.POST:
        rollno=request.POST["rollno"]
        rollno=int(rollno)
        result=results.get(rollno,"Not found")
        


    return render(request,"result.html",{"rollno":rollno,"result":result})

def resultviews(request):
    results={1:{"name":"popat","physics":90,"chemistry":89,"maths":23},2:{"name":"Bhide","Physics":59,"chemistry":90 , "math":94}}
    result=""
    rollno=0

    if request.POST:
        rollno=request.POST["rollno"]
        rollno=int(rollno)
        result=results.get(rollno,"Not found")

    return render(request,"result1.html",{"result":result,"rollno":rollno})

def resultclass2(request):
    class_2={1:{"name":"Aman","Age":6,"subject":{"English":65,"Hindi":35,"Science":89,"Math":65}},
                2:{"name":"Raman","Age":7,"subject":{"English":53,"Hindi":66,"Science":82,"Math":55}},
                 3:{"name":"Akash","Age":6,"subject":{"English":65,"Hindi":53,"Science":87,"Math":45}},
                  4:{"name":"Ram","Age":7,"subject":{"English":55,"Hindi":54,"Science":88,"Math":25}}, 
                  5:{"name":"Getta","Age":8,"subject":{"English":35,"Hindi":55,"Science":86,"Math":95}},
                  6:{"name":"Reta","Age":5,"subject":{"English":25,"Hindi":59,"Science":85,"Math":58}},}


    result=""
    rollno=0

    if request.POST:
        rollno=request.POST["rollno"]
        rollno=int(rollno)
        result=class_2.get(rollno,"not found")
        
    return render(request,"result2.html",{"rollno":rollno,"result":result})


