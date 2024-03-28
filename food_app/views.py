from django.http import HttpResponse
from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate ,login,logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.paginator import Paginator
from math import*
from django.core.mail import send_mail




# Create your views here.
def home(request):
    data=dish.objects.all()
    data1=showoff.objects.all()
    data2=banner.objects.all()
    data3=branch.objects.all()
    data4=show_video.objects.all()
    pg=Paginator(data1,4)
    page_num=request.GET.get('page')
    page=pg.get_page(page_num)
    chunk=4
    context={
        'count':pg.count,
        'page':page,
        'chunk':ceil(pg.count/chunk),
        'df':data,
        'df1':data2,
        'df2':data3,
        'df3':data4,
    }
    # data2=testimonial.objects.all()
    return render(request,'index.html',context)#'df2':data2})

def signup(request):
    if request.method == 'POST':
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        user_name=request.POST['username']
        Email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['confirm_password']
        img = request.FILES.get('profile_image', None)
        if password1==password2:
            if User.objects.filter(email=Email).exists():
                messages.info(request,'Account with this email already exists')
            elif User.objects.filter(username=user_name).exists():
                messages.info(request,' username already exists')
            else:
                user=User.objects.create_user(username=user_name,password=password1,email=Email,first_name=fn,last_name=ln)
                user_profile = profile.objects.create(user=user, profile_image=img)
                messages.info(request, 'You have successfully signed up!')
                return redirect("login")
        else:
            messages.info(request,"Both Password is not same")  
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
           auth.login(request,user)
           return redirect('/')
        else:
            messages.info(request,'Incorrect credentials')
    return render(request,'login.html')

def product(request):
    product=dish.objects.all()
    return render(request,'product.html',{'product':product})
def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):        
    return render(request,'about.html')

def pay(request):
    return render(request,'pay.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact.objects.create(name=name, email=email, message=message)
        return HttpResponse("<h3>Thank You For Contacting Us ,Someone from Our Team Will Contact You Soon!</h3>")
    return render(request, 'contact.html') 
