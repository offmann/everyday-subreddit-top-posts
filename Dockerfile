FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
ENV REDDIT_CLIENT_ID=<your client ID>
ENV REDDIT_CLIENT_SECRET=<your client secret>

COPY . /app

CMD [ "airflow", "scheduler" ]
