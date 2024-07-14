from .import views
from django.urls import path,re_path
from django.views.static import serve


urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('pay',views.pay, name='pay'),
    path('about',views.about, name='about'),
    path('product',views.product, name='product'),
    path('contact',views.contact_us, name='contact'),
    path('testimonial', views.testimonials, name='testimonial'),
    path('profile',views.user_profile, name='profile'),
    re_path(r'^dishimage/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]




