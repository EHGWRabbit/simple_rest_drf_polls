# simple_rest_drf_polls

###Installation

open terminal

pip install pipenv

mkdir polls

cd polls

clone https://github.com/EHGWRabbit/simple_rest_drf_polls.git

cd simple_rest_drf_polls-master

pipenv shell

pipenv install django==2.2.10

pipenv install coreapi==2.3.3

pipenv install pyyaml==5.1

pipenv install django-rest-swagger==2.2.0

pipenv install djangorestframework

python manage.py runserver

open browser

go to localhost:8000 (alt:127.0.0.1:8000)
