# Docker compose command

```shell
docker-compose run -rm app sh -c "python manage.py collectstatic"
```

* _docker-compose_ runs a Docker Corrmpose command
* _run_ will start a specific container defined
* _--rm_ removes the container
* _app_ is the name of the service
* _sh -c_ passes in a shell command 
  * This command basically says "We want to run a single command on our container" 
* _"python manage.py collectstatic"_ 
  * Command to run inside container