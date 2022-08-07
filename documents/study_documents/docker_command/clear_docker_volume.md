# Clear docker volume command

> ### After these command is executed,
> ### PostgresSQL data is going to be cleared

<br>
<br>

### Commands for DB clearing 

1. ls docker volume
```shell
docker volume ls
```

2. Remove docker volume
```shell
docker volume rm study_django_rest_framework_dev-db-data
```

3. Remove docker-compose data and remove docker volume again 
```shell
docker-compose down
```
```shell
docker volume rm study_django_rest_framework_dev-db-data
```


### Command for Migrate
```shell
docker-compose run --rm app sh -c \
"python manage.py wait_for_db && python manage.py migrate"
```