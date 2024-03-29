FROM python:3.11

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 8000
