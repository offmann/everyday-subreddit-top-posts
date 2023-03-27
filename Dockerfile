FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

ARG REDDIT_CLIENT_ID
ARG REDDIT_CLIENT_SECRET

ENV REDDIT_CLIENT_ID=$REDDIT_CLIENT_ID
ENV REDDIT_CLIENT_SECRET=$REDDIT_CLIENT_SECRET

COPY . /app

CMD [ "airflow", "scheduler" ]
