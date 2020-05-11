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
```

https://nickjanetakis.com/blog/docker-tip-45-docker-compose-stop-vs-down