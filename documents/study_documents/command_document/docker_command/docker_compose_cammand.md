# Docker compose command

1. How to execute linux(python-alpine) command in docker container

```shell
docker-compose run -rm app sh -c "python manage.py collectstatic"
```

* _docker-compose_ runs a Docker Compose command
* _run_ will start a specific container defined
* _--rm_ removes the container
* _app_ is the name of the service
* _sh -c_ passes in a shell command
    * This command basically says "We want to run a single command on our container"
* _"python manage.py collectstatic"_
    * Command to run inside container

<br>

2. Linting

```shell
docker-compose run --rm app sh -c "flake8"
```

* flake8 package helps handle Linting
* Run it through Docker Compose

<br>

3. Execute Django Test

```shell
docker-compose run --rm app sh -c "python manage.py test"
```

* Django test suite
* Setup tests per Django app
* Run tests through Docker Compose

<br>

4. Start Django project

```shell
docker-compose run --rm app sh -c "django-admin startproject app ."
```

<br>

5. Remove docker-compose container

```shell
docker-compose down 
```

6. Service start and stop

```shell
docker-compose up
```

```shell
docker-compose stop
```

<br>

7. Make new Django app

```shell
docker-compose run --rm app sh -c "python manage.py startapp appName"
```

<br>

8. Execute custom command

```shell
docker-compose run --rm app sh -c "python manage.py wait_for_db"
```

```shell
docker-compose run --rm app sh -c "python manage.py wait_for_db && flake8"
```

<br>


9. Migration command
```shell
docker-compose run --rm app sh -c "python manage.py makemigrations"
```
```shell
docker-compose run --rm app sh -c \
"python manage.py wait_for_db && python manage.py migrate"
```