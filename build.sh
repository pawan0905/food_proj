#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
echo "Build completed successfully."
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@email.com
export DJANGO_SUPERUSER_PASSWORD="adpass"  # Replace with your actual password

# Create superuser if it doesn't exist
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL || true

# Clear sensitive environment variables
unset DJANGO_SUPERUSER_PASSWORD