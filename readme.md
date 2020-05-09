# Cách sử dụng cơ bản

## Run app
```
python3.6 -m venv env
source env/bin/activate
pip install -r requirements/dev.txt
python manage.py migrate
python manage.py runserver
```

## Build & Run 
```
docker build -t thanhnb-django:v1 .
docker run -it -p 8080:8080 thanhnb-django:v1
docker-compose build
docker-compose up -d
```

https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

