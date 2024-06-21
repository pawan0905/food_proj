from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth import authenticate ,login,logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.paginator import Paginator
from math import*
from django.core.mail import send_mail
import cloudinary.uploader


# Create your views here.
def home(request):
    if request.session.has_key('uid'):
         data=dish.objects.all()
         data1=showoff.objects.all()
         data2=banner.objects.all()
         data3=branch.objects.all()
         data4=show_video.objects.all()
         data5=Testimonial.objects.all()
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
         'testimonial':data5,
         }
        # data2=testimonial.objects.all()
         return render(request,'index.html',context)#'df2':data2})
    else:
        return redirect('login')


def signup(request):
    if request.method == 'POST':
        # Extract form data
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm_password']
        img = request.FILES.get('profile_image', None)

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Account with this email already exists')
            elif User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username already exists')
            else:
                # Create the user
                user = User.objects.create_user(username=user_name, password=password1, email=email, first_name=fn, last_name=ln)

                # Upload profile image to Cloudinary
                if img:
                    cloudinary_response = cloudinary.uploader.upload(img)
                    profile_image_url = cloudinary_response['secure_url']
                else:
                    profile_image_url = None

                # Create user profile
                user_profile = profile.objects.create(user=user, profile_image=profile_image_url)

                messages.info(request, 'You have successfully signed up!')
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")

    return render(request, 'signup.html')

def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
           auth.login(request,user)
           request.session['uid']=request.POST['username']
           return redirect('/')
        else:
            messages.info(request,'Incorrect credentials')
    return render(request,'login.html')

def product(request):
    product=dish.objects.all()
    return render(request,'product.html',{'product':product})
def logout(request):
    del request.session['uid']
    auth.logout(request)
    return redirect('login')

def about(request):        
    return render(request,'about.html')

def pay(request):
    return render(request,'pay.html')

@login_required
def testimonials(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        message = request.POST.get('message')
        # Assuming you have a profile associated with the user
        profile = request.user.profile  # Assuming profile is related to the user

        # Create the testimonial object
        testimonial = Testimonial.objects.create(
            author=request.user,
            profile=profile,
            rating=rating,
            message=message
        )
        
        # Redirect the user after creating the testimonial
        return redirect('/')  # Change 'index' to the name of your index page
    else:
        # Render the template if it's a GET request
        return render(request, 'testimonial.html',{})

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact.objects.create(name=name, email=email, message=message)
        return HttpResponse("<h3>Thank You For Contacting Us ,Someone from Our Team Will Contact You Soon!</h3>")
    return render(request, 'contact.html') 

def user_profile(request):
    return render(request, 'profile.html')
