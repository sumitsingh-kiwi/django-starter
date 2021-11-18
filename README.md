[![GitHub Super-Linter](https://github.com/sumitsingh-kiwi/django-starter/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)
## Steps to setup the project:

### Manual setup

* create a python3.8 environment and activate it
* inside the main directory, create a .env file as follow and then edit the value according to the need
    > cp .env.sample .env
* install all the requirements 
    > pip install -r requirements.txt
* Please look into the accounts > models > auth.py , Please do the required changes as per 
  your project requirements, and then do the migrations
    > python manage.py makemigrations
* and now time to migrate the changes
    > python manage.py migrate
* then run the server
    > python manage.py runserver

### Docker Setup

#### Create env file:-  
 create .env file parallel to .env_sample and change the values accordingly.

#### Install docker and docker composer:
[https://docs.docker.com/install/linux/docker-ce/ubuntu/](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

[https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
###### 1: Production Environment 
	docker-compose -f docker-compose.yml up -d --build
###### 2: Development Environment
	docker-compose -f docker-compose-dev.yml up -d --build
###### 3: Qa Environment
	docker-compose -f docker-compose-qa.yml up -d --build
###### 4: Staging Environment
	docker-compose -f docker-compose-staging.yml up -d --build
###### 4: Local Environment
	Change database credential in .env file
	
	DB_NAME=postgres  
	DB_USERNAME=postgres  
	DB_PASSWORD=''  
	DB_HOST=db  
	DB_PORT=5432 
	
	docker-compose -f docker-compose-local.yml up -d --build
	
	Now you can access the server on 8004 port 
