# DB Release Tasks

python web/manage.py makemigrations --noinput
python web/manage.py migrate --noinput


# Alogia Release Tasks

python web/manage.py algolia_applysettings
python web/manage.py algolia_clearindex
python web/manage.py algolia_reindex