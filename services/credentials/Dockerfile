FROM python:3.7-alpine

#RUN apt-get update && apt-get -y install netcat curl && apt-get clean

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
	curl \
	bash &&  rm  -rf /tmp/* /var/cache/apk/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#COPY config.yml ./
#COPY run.sh ./
#COPY credentials ./
#COPY utils.py ./
#COPY alembic.ini ./
COPY . ./

RUN pip3 install --upgrade pip
RUN pip3 install .

RUN chmod +x ./run.sh

CMD ["./run.sh"]