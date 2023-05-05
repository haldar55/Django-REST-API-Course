FROM alpine:latest
LABEL authors="Pratiksha"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
RUN apk add python3 py3-pip
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /code
WORKDIR /code
COPY . /code /code

RUN adduser -D phaldar
USER phaldar

EXPOSE 8000