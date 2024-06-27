<h1 align="center">Django UrlShortener Web App</h1>
<h3 align="center">A simple Url shortener App project - It is used to shorten URLs and generate short links making them easy to share.</h3>
<br />

### Overview

- [Overview](#overview)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Setup](#setup)
- [Getting ready](#getting-ready)
- [Author](#author)

<br />

### Demo

You can check out the functionality of the project using this link.

```
https://shorturl-kaoj.onrender.com/
```

<br />

### Tech Stack

- Django
- HTML
- CSS
- BOOTSTRAP
- JAVA SCRIPT
- GIT

<br />

### Features

- User Authentication
- DataBase Linked
- Track User's created Urls
- Fully Responsive for all Devices
- Generating Short urls

<br />

### Setup

To get this repository, run the following command inside your git enabled terminal

```bash
git clone https://github.com/Techkrish1/ShortUrl.git
```

<br />

### Getting ready

Step by step commands on how to run this project on your computer

```
pip install virtualenv
```

1. Install Virtual Environment

```
pip install virtualenv
```

2. Create Virtual Environment

```
virtualenv venv
```

3. Activate virtual env

```
venv/Scripts/activate
```

4. install the dependencies of the project

```
pip install -r requirements.txt
```

5. Once you have installed django and other packages, go to the cloned repo directory and run the following command

```
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser for admin access and follow instruction, if not created one

```
python manage.py createsuperuser
```

7. Collect static files

```
python manage.py collectstatic
```

8. You can run the server :)

```
python manage.py runserver
```

<br>

### Author

- [@Gokula Krishnan](https://github.com/Techkrish1)
