# Beautiful scrapper

Scrap images from services

# Services available

freeimages.com

# How to start

* First of all, you will need python3 and make to be installed
* Now create a venv using python3 like this
```
python3 -m venv venv
```
* Now active the venv 
```
source venv/bin/activate
```
* Install the python dependencies 
```
make install
```
* Migrate the service to initialize the database
```
make migrate
```
* Create a superuser to access the django adminitration website
```
make createsuperuser
```
* Start the service
```
make start
```
* Now all you need to do is to use the service, by default it is running on port 8888, you can make your first request for this example by accessing the following link
```
http://localhost:8888/scrape/images/freeimages.com?search=dogs&limit=1000
```
* You can also access the django administration website to check your searches and images by using the following link
```
http://localhost:8888/admin
```
use the credentials created on createsuperuser step
* Finally you can run test cases using
```
make test
```