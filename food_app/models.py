from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images')

    def __str__(self):
        return self.user.username

class product_details(models.Model):
    price:int
    desr:str
    name:str
    img:str
    offer:bool

class dish(models.Model):
    name=models.CharField(max_length=100)
    desrp=models.CharField(max_length=200)
    price=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    offers=models.BooleanField()

    def __str__(self):
        return self.name

class showoff(models.Model):
    food_show=models.ImageField(upload_to='food_image')

class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class banner(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='banner')

    def __str__(self):
        return self.title

class branch(models.Model):
    city=models.CharField(max_length=100,blank=True)
    address=models.CharField(max_length=200,blank=True)
    email_address=models.EmailField()
    branch_contactno=models.CharField(max_length=20,blank=True)

class show_video(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='show_vid')

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(profile, on_delete=models.SET_NULL, null=True)
    rating = models.PositiveIntegerField()  
    message = models.TextField()
     
    def __str__(self):
        return self.author.username
    

    