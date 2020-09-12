from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def show(request):
    return render(request,'login.html') 

def login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print('login successful')
            return redirect('/')

def registration(request):
    if request.method == 'POST':
        first_name=request.POST['First_Name']
        last_name=request.POST['Last_Name']
        username=request.POST['Username']
        password1=request.POST['Password1']
        password2=request.POST['Password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('/')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('/accounts/show/')
        else:
            print('password not matching')  
            return render(request,'registration.html')

    else:
        return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/landing')

def showregistration(request):
    return render(request,'registration.html')