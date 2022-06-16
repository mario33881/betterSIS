FROM python:3.7-slim

ARG USER=www
ARG USER_ID=1000
ARG GROUP_ID=1000

ENV USER=$USER
ENV DEBIAN_FRONTEND=noninteractive

COPY ./bettersis /home/$USER/bettersis/bettersis/
COPY ./requirements.txt /home/$USER/bettersis/

RUN addgroup --gid $GROUP_ID $USER \
    && adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USER \
    && apt-get update \
    && apt-get install -y wget rsyslog \
    && sed -i '/imklog/s/^/#/' /etc/rsyslog.conf \
    && wget https://github.com/JackHack96/logic-synthesis/releases/download/1.3.6/sis_1.3.6-1_amd64.deb \
    && dpkg -i sis_1.3.6-1_amd64.deb \
    && rm sis_1.3.6-1_amd64.deb \
    && apt-get remove -y wget \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r "/home/$USER/bettersis/requirements.txt" \
    && mkdir /data \
	&& chmod -R 0777 /data

WORKDIR /data

ENTRYPOINT service rsyslog start && su $USER --command "python /home/$USER/bettersis/bettersis/bettersis.py"

VOLUME /data
