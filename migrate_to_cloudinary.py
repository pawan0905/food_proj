import os
import django
from django.core.wsgi import get_wsgi_application
import cloudinary
from cloudinary.uploader import upload

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_project.settings')
django.setup()
application = get_wsgi_application()

from food_app.models import profile, dish, showoff, banner, show_video

def migrate_files():
    # Cloudinary configuration
    cloudinary.config(
        cloud_name='dz5ezf3xf',
        api_key='519955659836142',
        api_secret='iuGU2LkMg40KMMyCxAugFZCaQd0'
    )
    # Migrate profile images
    profiles = profile.objects.all()
    for prof in profiles:
        if prof.profile_image:
            # Upload profile_image to Cloudinary
            cloudinary_result = upload(prof.profile_image.path)
            prof.profile_image = cloudinary_result['secure_url']
            prof.save()

    # Migrate dish images
    dishes = dish.objects.all()
    for dish_obj in dishes:
        if dish_obj.img:
            # Upload img to Cloudinary
            cloudinary_result = upload(dish_obj.img.path)
            dish_obj.img.name = cloudinary_result['public_id']
            dish_obj.save()

    # Migrate showoff images
    showoffs = showoff.objects.all()
    for show in showoffs:
        if show.food_show:
            # Upload food_show to Cloudinary
            cloudinary_result = upload(show.food_show.path)
            show.food_show.name = cloudinary_result['public_id']
            show.save()

    # Migrate banner videos
    banners = banner.objects.all()
    for ban in banners:
        if ban.video_file:
            # Upload video_file to Cloudinary
            cloudinary_result = upload(ban.video_file.path, resource_type="video")
            ban.video_file.name = cloudinary_result['public_id']
            ban.save()

    # Migrate show videos
    show_videos = show_video.objects.all()
    for show_vid in show_videos:
        if show_vid.video:
            # Upload video to Cloudinary
            cloudinary_result = upload(show_vid.video.path, resource_type="video")
            show_vid.video.name = cloudinary_result['public_id']
            show_vid.save()

if __name__ == '__main__':
    migrate_files()
