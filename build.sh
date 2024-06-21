#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Migrate database
python manage.py migrate

# Set environment variables
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@email.com
export DJANGO_SUPERUSER_PASSWORD="adpass"  # Replace with your actual password

# Create superuser if it doesn't exist
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL || true

# Clear sensitive environment variables
unset DJANGO_SUPERUSER_PASSWORD

# Additional steps for Cloudinary setup
export CLOUDINARY_CLOUD_NAME=dz5ezf3xf
export CLOUDINARY_API_KEY= 111922656567258
export CLOUDINARY_API_SECRET= VfbNTaPgMl2aaikdFjyUnB_M48Q

python migrate_to_cloudinary.py

echo "Build completed successfully."
