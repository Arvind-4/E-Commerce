python manage.py makemigration --noinput
python manage.py migrate --noinput

python manage.py collectstatic -i rest_framework -i flags --no-input