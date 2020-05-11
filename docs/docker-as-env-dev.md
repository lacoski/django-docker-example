# Tải ENV
```
sudo docker pull ubuntu
```

# Chạy container ubuntu với port
```
sudo docker run -i -t -p 127.0.0.1:8000:8000 ubuntu
```

# Mount dev env với container

```
sudo docker run -i -t -p 127.0.0.1:8000:8000 \
-v /home/thanhnb/data/repos/GitDocker/django-docker-example:/home/code ubuntu

docker exec -it eade101e0aa3 python manage.py shell
```

https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes