FROM python:3.7-alpine

RUN apk update && apk upgrade && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add --no-cache \
	git \
	openssl-dev \
	lz4-dev \
	cyrus-sasl-dev \
	libldap \
	postgresql-dev \
	nano \
	openldap-dev \
	pcre-dev \
	bash &&  rm  -rf /tmp/* /var/cache/apk/*


RUN mkdir /app
COPY . /app
WORKDIR /app

COPY config.yml /app/config.yml
COPY run.sh /app/run.sh

#RUN chmod +x /app/run.sh
RUN pip3 install --upgrade pip
RUN pip3 install .

EXPOSE 8000

RUN  /app/run.sh


