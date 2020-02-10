FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV LISTEN_PORT 8075
EXPOSE 8075

COPY ./app /app

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt