python web/manage.py makemigrations --noinput
python web/manage.py migrate --noinput

python web/manage.py collectstatic -i rest_framework -i flags --no-input