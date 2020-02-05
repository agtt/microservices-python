Marketplace Microservices - OPLOG
==================

Woocommerce, N11, Hepsiburada, Gittigidiyor, Amazon,EPTT Webservices

Pre-requisities
--------------

* Docker engine installed on the host server
* `docker-compose` installed on the host server


How to build the application
----------------------------

```bash
$ docker-compose build
```

How to run the application
--------------------------

In case of the first run:

```bash
$ cd scripts
$ ./init_sentry.sh
```

```bash
$ docker-compose up -d
```

The application Swagger UI is accessible at http://0.0.0.0:8000

How to stop and remove the application
--------------------------------------

```bash
$ docker-compose down
```

Credentials
-----------

Username: demo

Password: demo
