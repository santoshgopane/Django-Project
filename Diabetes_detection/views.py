from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('Hello, World!')
    return render(request,'New.html')
def adding(request):
    value1 = int(request.POST["num1"])
    value2 = int(request.POST["num2"])
    return render(request,'result.html',{'res':value1+value2})