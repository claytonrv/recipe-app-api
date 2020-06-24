FROM python:3.7-alpine
LABEL maintainer="Clayton Veras - YTO Tecnologia github:(@claytonrv)"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=app.settings

#Installing build only dependencies
RUN apk update && apk add gcc musl-dev postgresql-dev python3-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
