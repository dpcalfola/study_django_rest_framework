# test container deploy command

```shell
docker run \
-itd \
--name drf_test_container \
study_django_rest_framework_app
```

<br>

```shell
docker start drf_test_container
```

<br>






### Get inside to alpine linux
```shell
docker exec -it drf_test_container sh
```

<br>






### Create test container and get inside to linux

```shell
docker run \
-itd \
--name drf_test_container \
study_django_rest_framework_app &&
docker exec -it drf_test_container sh

```

<br>






### Stop and remove test drf_test_container

```shell
docker stop drf_test_container && docker rm drf_test_container
```


