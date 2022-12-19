#!/bin/bash

echo "Upgrade pip..."
python3.9 -m pip install --upgrade pip

echo "Installing dependencies..."
python3.9 -m pip install -r requirements.txt

echo "Migrating database..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Creating superuser..."

DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

python3.9 manage.py createsuperuser \
    --email $DJANGO_SUPERUSER_EMAIL \
    --noinput || true

echo "Running npm install..."
npm run i

echo "Running npm Production..."
npm run production

echo "Clear Cache..."
rm -rf apps/www

echo "Collecting static files..."
python3.9 manage.py collectstatic -i rest_framework -i flags --noinput --clear