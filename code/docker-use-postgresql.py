## ```bash
docker pull postgres
## ```


## ```bash
docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
## ```

## ```bash
docker start my-postgres
## ```


## ```bash
docker stop my-postgres
## ```

## ```bash
docker rm my-postgres
## ```


## ```bash
docker exec -it my-postgres bash
## ```


## ```bash
vi /var/lib/postgresql/data/postgresql.conf
## ```


## ```
listen_addresses = '*'
## ```


## ```bash
service postgresql restart
## ```
