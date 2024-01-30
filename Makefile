install:
	python -m pip install -r requirements.txt

createsuperuser:
	python manage.py createsuperuser

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

start:
	python manage.py runserver 0.0.0.0:8888

test:
	python manage.py test
