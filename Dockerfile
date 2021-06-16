FROM python:3.8.7-slim-buster

MAINTAINER Anatoly Basyuk <a.basyuk@meotyda.com>

# SYSTEM ENV
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV PATH "/opt/app/bin:$PATH"


ENV DJANGO_SETTINGS_MODULE 'system.settings'
ENV DJANGO_DEBUG False

ENV POSTGRESQL_HOST 'postgresql'
ENV POSTGRESQL_DATABASE 'club'
ENV POSTGRESQL_USER 'postgres'
ENV POSTGRESQL_PASSWORD 'postgres'
ENV POSTGRESQL_PORT 5432

ENV BROKER_URL 'amqp://guest:guest@rabbitmq:5672//'

RUN set -ex \
    && BUILD_DEPS=" \
    gcc \
    make \
    curl \
    wget \
    build-essential \
    python-dev \
    libpcre3-dev \
    libpq-dev \
    postgresql-client \
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir -p \
    /opt/app/etc \
    /opt/app/python \
    /opt/app/python/static \
    /opt/app/python/media \
    /opt/app/log \
    /opt/app/run \
    /opt/app/bin


ADD ./src/requirements.txt /opt/app/python
ADD ./requirements/requirements-testing.txt /opt/app/python

RUN pip install --upgrade pip wheel setuptools \
    && pip install --no-cache-dir -r /opt/app/python/requirements.txt \
    && pip install --no-cache-dir -r /opt/app/python/requirements-testing.txt

COPY ./src /opt/app/python
COPY ./etc /opt/app/etc
COPY ./bin /opt/app/bin

RUN chmod -R 644 /opt/app/etc
RUN chmod -R +x /opt/app/bin

VOLUME '/opt/app/etc'
VOLUME '/opt/app/python'
VOLUME '/opt/app/python/media'
VOLUME '/opt/app/python/static'
VOLUME '/opt/app/log'
VOLUME '/opt/app/run'
VOLUME '/opt/app/bin'



WORKDIR /opt/app/python


EXPOSE 8000

#HEALTHCHECK --interval=5s --timeout=10s --retries=3 CMD wget -q --method=HEAD http://localhost/health/ || exit 1

ENTRYPOINT ["docker-entrypoint"]
CMD ["uvicorn"]
