### Start project
```shell
docker-compose run --rm app sh -c "django-admin startproject app ."
```

### Start app
```shell
docker-compose run --rm app sh -c "django-admin startapp tdd_practice"
```

### Run Test Code
```shell
docker-compose run --rm app sh -c "python manage.py test"
```

### Create Super User
```shell
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```