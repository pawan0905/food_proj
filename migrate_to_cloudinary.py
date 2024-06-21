import os
from django.core.wsgi import get_wsgi_application
import cloudinary.uploader

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_project.settings')
application = get_wsgi_application()

from food_app.models import profile, dish, showoff, banner, show_video

def migrate_files():
    # Profile images
    profiles = profile.objects.all()
    for prof in profiles:
        if prof.profile_image:
            cloudinary_result = cloudinary.uploader.upload(prof.profile_image.path)
            prof.profile_image.name = cloudinary_result['public_id']
            prof.save()
    
    # Dish images
    dishes = dish.objects.all()
    for dish_obj in dishes:
        if dish_obj.img:
            cloudinary_result = cloudinary.uploader.upload(dish_obj.img.path)
            dish_obj.img.name = cloudinary_result['public_id']
            dish_obj.save()
    
    # Showoff images
    showoffs = showoff.objects.all()
    for show in showoffs:
        if show.food_show:
            cloudinary_result = cloudinary.uploader.upload(show.food_show.path)
            show.food_show.name = cloudinary_result['public_id']
            show.save()
    
    # Banner videos
    banners = banner.objects.all()
    for ban in banners:
        if ban.video_file:
            cloudinary_result = cloudinary.uploader.upload(ban.video_file.path, resource_type="video")
            ban.video_file.name = cloudinary_result['public_id']
            ban.save()
    
    # Show videos
    show_videos = show_video.objects.all()
    for show_vid in show_videos:
        if show_vid.video:
            cloudinary_result = cloudinary.uploader.upload(show_vid.video.path, resource_type="video")
            show_vid.video.name = cloudinary_result['public_id']
            show_vid.save()

if __name__ == '__main__':
    migrate_files()
