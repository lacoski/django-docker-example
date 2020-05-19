# Run prod env bằng CMD

```
docker build -f ./Dockerfile.prod -t web_django:cmd1 ./

docker pull postgres:12.0-alpine

docker volume create postgres_data_db
docker volume create static_volume_web

POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
POSTGRES_DB=hello_django_prod

docker run -itd -e "POSTGRES_USER=hello_django" -e "POSTGRES_PASSWORD=hello_django" -e "POSTGRES_DB=hello_django_prod" postgres:12.0-alpine

DEBUG=0
SECRET_KEY=change_me
DJANGO_ALLOWED_HOSTS=*
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_prod
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres

docker run -itd -p 8888:8000 \
    -e "SECRET_KEY=please_change_me" -e "DEBUG=1" -e "DJANGO_ALLOWED_HOSTS=*" \
    -e "SQL_ENGINE=django.db.backends.postgresql" -e "SQL_DATABASE=hello_django_prod" \
    -e "SQL_USER=hello_django" -e "SQL_PASSWORD=hello_django" -e "SQL_HOST=172.17.0.2" \
    -e "SQL_PORT=5432" -e "DATABASE=postgres" \
    web_django:cmd1 python /home/app/web/manage.py runserver 0.0.0.0:8000

docker run -itd -p 8888:8000 \
    -e "SECRET_KEY=please_change_me" -e "DEBUG=1" -e "DJANGO_ALLOWED_HOSTS=*" \
    -e "SQL_ENGINE=django.db.backends.postgresql" -e "SQL_DATABASE=hello_django_prod" \
    -e "SQL_USER=hello_django" -e "SQL_PASSWORD=hello_django" -e "SQL_HOST=172.17.0.2" \
    -e "SQL_PORT=5432" -e "DATABASE=postgres" \
    -v static_volume_web:/home/app/web/static \
    web_django:cmd1 gunicorn project.wsgi:application --bind 0.0.0.0:8000

docker build -f ./nginx/Dockerfile.cmd -t nginx:cmd1 ./nginx

docker run -itd -p 1337:80 \
    -v static_volume_web:/home/app/web/static \
    nginx:cmd1
```