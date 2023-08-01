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

