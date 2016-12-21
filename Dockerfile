FROM python:3.5.2-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=$PYTHONPATH:/srv/app

RUN mkdir -p /srv/app
WORKDIR /srv/app

ADD requirements.txt /srv/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ADD . /srv/app

EXPOSE 8000
CMD gunicorn prev:app --log-file=-
