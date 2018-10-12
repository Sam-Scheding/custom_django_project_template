# custom_django_project_template
A custom Django project template with some boiler plate code prewritten and custom commands to make life easier

# Overview
By default the project will run with the development settings. To change this for production edit manage.py

## Custom Commands
The project template includes a number of custom commands to make development easier. They are included in the
`dev` app, and as such will not be usable if the project is run with the deployment settings. The deployment
settings file cannot be used without configuring a separate SECRET_KEY. This is by design; generate a new secret
key by running `python manage.py gensecretkey`.

The complete list of custom commands are:

  - `python manage.py r`: Shortcut for `python manage.py runserver`
  - `python manage.py m`: Shortcut for `python manage.py makemigrations && python manage.py migrate`
  - `python manage.py resetdb`: Delete all migrations folders. WARNING: Only to be used for development purposes
  - `python manage.py gensecretkey`: Generate a new valid Django secret key

## Static and media
The static and media settings are preset in the development settings file but not in the deployment settings file.

## Apps
The template contains a number of prewritten apps to make starting a project quicker. They are in the `apps/` directory. It is advised that you continue this workflow so the project directory doesn't become messy.

  - `dev`: Contains the custom management commands above
  - `custom`: Contains some modules to extend the functionality of Django. For example the TitleMixin that allows you to set a page title from the view.
  - `main`: A basic hello world Django app to be extended upon.

# Usage:

To create a new Django project using this custom template, simply run:

`$ django-admin startproject <project_name> --template=https://github.com/Sam-Scheding/custom_django_project_template/archive/master.zip`
