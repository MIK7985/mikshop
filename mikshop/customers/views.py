from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signout(request):
    logout(request)
    return redirect('home')
def account_show(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            print(request.POST)
            #create uder accounts
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            #creats customer account
            )
            customer=Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            success_message="user registerd successfully"
            messages.success(request,success_message)                
        except Exception as e:
            error_message="duplicate username or invalid input"
            messages.error(request,error_message)    
    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            error_message="invalid credentials"
            messages.error(request,error_message)  

    return render(request,'account.html',context)
