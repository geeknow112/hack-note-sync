# ```bash
docker pull nginx
# ```


# ```bash
docker run -d -p 80:80 nginx
# ```


# ```bash
docker ps
# ```


# ```Dockerfile
FROM nginx

COPY nginx.conf /etc/nginx/nginx.conf
# ```


# ```bash
docker build -t my-nginx .
# ```


# ```yaml
version: '3'

services:
  nginx:
    image: nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - app

  app:
    image: my-app
    ports:
      - "3000:3000"
# ```
