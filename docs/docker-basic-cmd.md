## Dừng toàn bộ và xóa tất

```
docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
```

## Xem log container realtime

```
docker logs -f 486cce331130
```

## Xóa Image build lỗi
```
docker rmi $(docker images -f "dangling=true" -q)
```

## Xoá tất cả các volume không sử dụng
```
docker volume prune
```

https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/