# E-commerce

A Simple E-commerce build on Django 4, Solid js, and TailWind! .

## Stack

- [Solid Js](https://www.solidjs.com/) - A Reactive JavaScript Library.
- [Django](https://www.djangoproject.com/) - Django makes it easier to build better web apps more quickly and with less code.
- [Vite](https://vitejs.dev/) - Next Generation Frontend Tooling.
- [Typescript](https://www.typescriptlang.org/) - JavaScript with syntax for types.
- [Tailwind 3](https://tailwindcss.com/) - Rapidly build modern websites without ever leaving your HTML.
- [CockroachDB](https://www.cockroachlabs.com/) - A distributed SQL database designed for speed, scale, and survival.

### 

NOTE: Still Under Progress ...

## Project structure

```
$PROJECT_ROOT
│  
├── web  # Django file
│  
├── frontend  # Solid js App
│   
├── web/templates # Django Templates
│   
├── web/ accounts, carts, category, products, pages 
|	# Django Apps
│   
├── commands # shell commands.
```
---

### Get the Code

- Clone Repo

```
mkdir django_ecommerce
cd django_ecommerce
git clone https://github.com/Arvind-4/E-Commerce-.git .
```
- Create Virtual Environment for Python

```
pip install virtualenv
python -m venv .
```

- Activate Virtual Environment

```
source Scripts/activate
```

- Install Dependencies

```
pip install -r requirements.txt
```

- Make Migrations

```
python web/manage.py makemigrations
python web/manage.py migrate
```

####  For Frontend

- Install Dependencies

```
yarn install
```
- Install CSS for Django 

```
cd static-dev/css-dev
yarn install
```
- Now for Bundling Your Frontend + Django static

```
commands/bundle-frontend.sh 
```

**Run this Command in Your Root of the Project!**

- Now Run The Server

Open [localhost:8000](http://localhost:8000/) in Your Browser.
```
commands/run.sh 
```
<br/>

> **_NOTE:_**     Add Products by Navigating  Admin Page. <br/>
> Admin url => [admin/](http://localhost:8000/admin/)
