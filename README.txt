## BUILD

docker build -t myimage .

## RUN
docker run --name myimage --restart unless-stopped -d myimage
