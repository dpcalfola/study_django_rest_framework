FROM python:alpine3.16
LABEL maintainer="github.com/dpcalfola"

ENV PYTHONUNBUFFERED 1

#ENV TZ Asia/Seoul

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py_venv && \
    /py_venv/bin/pip install --upgrade pip && \
    /py_venv/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py_venv/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py_venv/bin:$PATH"

USER django-user