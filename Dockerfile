FROM python:3.10
LABEL maintainer="vitalikbashkiser@gmail.com"
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
