python web/manage.py makemigration --noinput
python web/manage.py migrate --noinput

python web/manage.py collectstatic -i rest_framework -i flags --no-input