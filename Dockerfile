


# temp stage para instalar linux con python incorporado
FROM python:3.10.6-slim-bullseye

WORKDIR /app

# para evitar warnings respecto al update de pip instalo la mas reciente
RUN python -m pip install --upgrade pip

# Instalo y actualizo todos los paquetes del SO 
RUN apt-get update -qq \
    && apt-get install --no-install-recommends --yes \
        build-essential \
        cron \
        vim \
        default-libmysqlclient-dev \
        # No remover las siguientes instalaciones si se usa la APP con mysql
        libmariadb3 \
    && rm -rf /var/lib/apt/lists/* \
    && python3 -m pip install --no-cache-dir mysqlclient \
    && apt-get autoremove --purge --yes \
        build-essential \
        default-libmysqlclient-dev



# Copio todos los directorios desde la maquina host al nuevo contenedor
COPY . .
COPY crontabfile /etc/cron.d/crontabfile
RUN chmod +x /etc/cron.d/crontabfile
RUN crontab /etc/cron.d/crontabfile


# run crond as main process of container
CMD ["cron", "-f"]


