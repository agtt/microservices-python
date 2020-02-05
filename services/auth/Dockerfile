FROM python:3.6-slim

RUN apt-get update && apt-get -y install netcat curl && apt-get clean

WORKDIR /app

COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./run.sh

CMD ["./run.sh"]