FROM python:3.10.0-alpine
LABEL authors="sayfullaev"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update && apk add postgresql-dev

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./