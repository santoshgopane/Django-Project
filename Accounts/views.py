from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):

    if request.method == 'POST':
        First_name = request.POST['fn']
        Last_name  = request.POST['ln']
        Username = request.POST['username']
        Email = request.POST['email']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']

        if password1 == password2:
            if User.objects.filter(username=Username).exists():
                messages.info(request,'Username Taken!')
                return redirect('reg')
            elif User.objects.filter(email=Email).exists():
                messages.info(request,'Email Taken!')
                return redirect('reg')
            else:    
                user_create = User.objects.create_user(username=Username,email=Email,password=password1,first_name=First_name,last_name=Last_name)
                user_create.save()
                messages.info(request,'User Created!')
                return redirect('Login')
        else:
            messages.info(request,'Password Not matching!')
            return redirect('reg')
    else:
        return render(request,'Registration.html')

def login(request):

    if request.method == 'POST':
        
        Username = request.POST['username'] 
        Password = request.POST['pwd']

        User = auth.authenticate(username=Username,password=Password)

        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            messages.info(request,'Incorrect Credentials!')
            return redirect('Login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')