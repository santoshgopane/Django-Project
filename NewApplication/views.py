from django.shortcuts import render
from django.http import HttpResponse
from . models import blogging
# Create your views here.

def homepage(request):

    # dest1 = blogging()
    # dest1.name = '"Er. Santosh Gopane"'
    # dest1.image = '2.jpg'
    # dest1.desc = 'This is the first description'

    # dest2 = blogging()
    # dest2.name = '"Er. San Gopane"'
    # dest2.image = '1.jpg'
    # dest2.desc = 'This is the second description'

    # dest3 = blogging()
    # dest3.name = '"Er. Santro Gopane"'
    # dest3.image = '3.jpg'
    # dest3.desc = 'This is the third description'

    # dests = [dest1,dest2,dest3]
    
    dests = blogging.objects.all() 

    return render(request,'index.html',{'Destn':dests})
    # return HttpResponse('Checking new application Working!')
    # return render(request,'index.html',{'name':'Santosh Gopane'})