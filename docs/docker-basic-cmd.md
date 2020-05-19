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