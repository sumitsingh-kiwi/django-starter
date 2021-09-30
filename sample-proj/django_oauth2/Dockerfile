FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN apt update
RUN apt install -y gdal-bin python-gdal python3-gdal
WORKDIR /usr/src/app
