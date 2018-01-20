FROM python:3.5

ENV DEBIAN_FRONTEND noninteractive

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update \
  && apt-get clean \
  && pip install --no-cache-dir -r /tmp/requirements.txt


RUN mkdir -p /app ; \
    mkdir -p /app/logs;


ADD src/ /app/
WORKDIR /app

CMD python3 main.py
