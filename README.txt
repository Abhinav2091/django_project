#create a virtual env for python command
py -m venv ./venv   #here .venv is dir path and folder name you want to create the virtual env

#to activate virtual env in git bash
source ./venv/Scripts/activate

run activate to activate and deactivate to deactivate

now install django in virtual env
pip install django

few django commands
django-admin
#to create project
django-admin startproject projectname .

use gitigrone.io site to add ignore file a per the framework

#command to run server
py manage.py runserver

by default db is sql_lite

create project for static pages
py manage.py startapp pages

install autopep8
pip install autopep8

#use pip for packges needed for db configuration
pip install psycopg2
pip install psycopg2-binary

#for default db migrante
 py manage.py migrate #to chek if db works fine return ok
 py manage.py makemigrations

 #just to check sql query
  py manage.py sqlmigrate appname file name that get created after make migrations

  #create super user
  py manage.py createsuperuser to login into /admin

  #install pylint
  pip install pylint-django