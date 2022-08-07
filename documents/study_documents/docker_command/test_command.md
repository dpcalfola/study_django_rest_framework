# Test commands

1. Execute test
```shell
docker-compose run --rm app sh -c "python manage.py test"
```

2. Execute test and linting
```shell
docker-compose run --rm app sh -c "python manage.py test && flake8"
```