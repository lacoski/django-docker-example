```
docker-compose -f docker-compose-deploy.yml exec db psql --username=hello_django --dbname=hello_django_dev


docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
docker-compose -f docker-compose-deploy.yml build
docker-compose -f docker-compose-deploy.yml up -d
```