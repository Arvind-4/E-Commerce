# E-commerce

A Simple E-commerce build on Django 4, Solid js, and TailWind! .

## Stack

- [Solid Js](https://www.solidjs.com/) - A Reactive JavaScript Library.
- [Django](https://www.djangoproject.com/) - Django makes it easier to build better web apps more quickly and with less code.
- [Vite](https://vitejs.dev/) - Next Generation Frontend Tooling.
- [Typescript](https://www.typescriptlang.org/) - JavaScript with syntax for types.
- [Tailwind 3](https://tailwindcss.com/) - Rapidly build modern websites without ever leaving your HTML.
- [CockroachDB](https://www.cockroachlabs.com/) - A distributed SQL database designed for speed, scale, and survival.


## Project structure

```
$PROJECT_ROOT
│  
├── apps/web  # Django Backend
│  
├── apps/www  # Solid js App
│   
├── apps/templates # Django Templates
│   
├── apps/web/apps/ accounts, carts, category, products, pages # Django Apps
│   
├── requirements # Python Requirements
│
├── testing # Jupyter Notebook for Testing
│
├── data/products.json # Sample Data
│
├── app.py # Entry Point for Django Backend
│
├── vercel.json # Vercel Config file
│
├── manage.py # Run Django Commands
│
├── package.json # npm commands.
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

```sh
pip install virtualenv
python -m venv .
```

- Activate Virtual Environment

```sh
source Scripts/activate
```
**Window Users use: `.\Scripts\activate`**

- Install Dependencies

```sh
pip install -r requirements.txt
```

- Make Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

####  For Frontend

- Install Dependencies

```
npm run i
```

- Run Dev Server

```
npm run dev
```

- Now for Bundling Your Frontend + Django static

```
npm run production
```

**Run Both Django and Vite Server for Hot Reload in Your Project Root**

Open [localhost:8000](http://localhost:8000/) in Your Browser.

<br/>

> **_NOTE:_**     Add Products by Navigating  Admin Page. <br/>
> Admin url => [admin/](http://localhost:8000/admin/)