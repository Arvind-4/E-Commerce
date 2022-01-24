rm -rf dist/ 
yarn build:production
cd static-dev/css-dev/
yarn build:production
cd ..
cd ..
rm -rf static && python manage.py collectstatic -i css-dev -i admin -i rest_framework --no-input