#create a virtual env for python command
py -m venv ./venv   #here .venv is dir path and folder name you want to create the virtual env

#to activate virtual env
.\venv\Scripts\activate 

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
