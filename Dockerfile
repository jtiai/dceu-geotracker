FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGOCON_APP_VERSION 1.0.0

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gdal-bin \
    proj-bin \
    libgeos-c1v5 \
 && rm -rf /var/lib/apt/lists/*

RUN pip install pipenv
COPY ./geotracker/Pipfile* /app/
RUN pipenv install

CMD ["/app/start.sh"]
