# ready to use Django Project with Oauth2/Email-settings/celery-settings/push-notifications

## Steps to use this project:

* create a python3.8 environment and activate it
* inside the main directory, create a .env file as follow and then edit the value according to the need
    > cp .env.sample .env
* install all the requirements 
    > pip install -r requirements.txt
* Please look into the accounts > models > auth.py , Please do the required changes as per 
  your project requirements, and then do the migrations
    > python manage.py makemigrations accounts --name=migrations
* and now time to migrate the changes
    > python manage.py migrate
* Please set the ROOT_URLCONF variable in settings > base.py according to your project name
* then run the server
    > python manage.py runserver
    > python manage.py loaddata fixtures/notification_type.json
