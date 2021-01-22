# Building Rest APIs for BookStore App
1. Install MongoDB Server.
2. Install Anaconda or Python

## Install Django Rest Framework
* To install this package run this command in the terminal
* `pip install djangorestframework`
> Note -
>  * After installation enter `django-admin` in the terminal to check whether the path variable is updated properly.
>  * If it doesn't work go to `$AppData\Roaming\Python\Python39\Scripts` and add this filepath into the **PATH** environment variable.

## Creating the REST API project
* Create an Empty folder with name `BookStore`
* Next enter the following command into terminal
  - `django-admin startproject BookStore`
* This will create a template for the Rest API Framework
* Now to connect your App to MongoDB you will need `Djongo` connector
  - `pip install djongo`

### Setting up DB Connection
* Open the `BookStore\settings.py`. Under the DATABASES map enter the following details:
```Python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'bookstore',
        'HOST': '127.0.0.1',
        'PORT': 27017,
    }
}
```

### Adding RestFramework and RestAPI App to the Django project
* Your folder structure will be as follows -
> BookStore
> \BookStore

* Now to create your BookStoreApp enter
`python manage.py startapp BookStoreApp` into terminal
* Go to `BookStore\settings.py`, find INSTALLED_APPS map and add the lines after the comment into the map
```Python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # DJANGO REST FRAMEWORK
    'rest_framework',
    # BOOKSTORE APPLICATION
    'BookStoreApp.apps.BookstoreappConfig'
]
```

# Creating REST API App

## IMPLEMENT THE DATA MODEL

Under the `BookStoreApp\models.py` you can implement the collections by using Classes. For example, Users class implement the user collection in MongoDB.

After implementing the classes you need to migrate these changes onto MongoDB

Run the following command to start migrations
`python manage.py makemigrations BookStoreApp`
You will get the following output -
```Text
Migrations for 'BookStoreApp':
  BookStoreApp\migrations\0001_initial.py
    - Create model BookStoreApp
```

## SERIALIZE AND DESERIALIZE Database

Refer the `BookStoreApp\serializers.py` to create serializers for the data models injected into MongoDB.

## API VIEWS

API Views will handle the REST CALLS to your app. Refer the `BookStoreApp\views.py` to get a gist of the calls defined that handle GET/PUT/POST/DELETE calls.

## ROUTE URLS TO VIEW FUNCTIONS

In the `BookStoreApp\urls.py` you can define which url pattern should route to the respective view functions.

Once the url patterns are added into the `BookStoreApp\urls.py` file. Update the `BookStore\urls.py` as follows:
```python
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('BookStoreApp.urls')),
]
```

# STARTING THE SERVER

Run the command into terminal
`python manage.py runserver`
