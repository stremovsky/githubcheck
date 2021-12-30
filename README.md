## Build
```
docker build -t myimage .
```

## Run
```
docker run --name myimage --restart unless-stopped myimage
```

## Start container and pass SLACK_API_TOKEN variable
```
docker run --name myimage -e SLACK_API_TOKEN=1234 --restart unless-stopped myimage
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
