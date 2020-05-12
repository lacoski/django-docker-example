```
docker-compose -f docker-compose-deploy.yml exec db psql --username=hello_django --dbname=hello_django_dev


docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
docker-compose -f docker-compose-deploy.yml build
docker-compose -f docker-compose-deploy.yml up -d

docker-compose -f docker-compose-prod.yml build
docker-compose -f docker-compose-prod.yml up -d
docker-compose -f docker-compose-prod.yml up -d --build

# Stop and Start
docker-compose -f docker-compose-prod.yml stop
docker-compose -f docker-compose-prod.yml start

# Start
docker-compose -f docker-compose-prod.yml up -d

# Stop và clear
docker-compose -f docker-compose-prod.yml down -v

# Cmd
docker-compose -f docker-compose-prod.yml ps
docker-compose -f docker-compose-prod.yml exec web python manage.py createsuperuser

docker-compose -f docker-compose-prod.yml images
docker-compose -f docker-compose-prod.yml logs

docker-compose -f docker-compose-prod.yml exec db psql --username=hello_django --dbname=hello_django_dev
docker-compose -f docker-compose-prod.yml exec db psql --username=hello_django --dbname=hello_django_prod
```

PS SQL
```
# List DB
\l

# List available databases
\c hello_django_prod

# List available tables
\dt

# Describe a table
\d auth_user

# List available schema
\dn

# Command history
\s

# Get help on psql commands
\?

# Query
select * from books_cbv_book;
```

Lưu ý:
- docker-compose stop: Dừng các container
- docker-compose down: Dừng + xóa các container + `-v` = xóa các volume

https://nickjanetakis.com/blog/docker-tip-45-docker-compose-stop-vs-down

https://docs.docker.com/compose/extends/

https://www.reddit.com/r/django/comments/bjgod8/dockerizing_django_with_postgres_gunicorn_and/