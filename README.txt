## Build
```
docker build -t myimage .
```

## Run
```
docker run --name myimage --restart unless-stopped myimage
```

## Run in background
```
docker run --name myimage --restart unless-stopped -d myimage
```

## Kill & remove leftovers
```
docker kill myimage
docker rm myimage
```
