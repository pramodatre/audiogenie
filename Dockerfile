# Dockerfile

# pull the official docker image
FROM python:3.10.14-slim

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install dependencies
RUN pip install -r requirements.txt
# RUN pip install poetry
# RUN poetry install