FROM python:3.5.2-alpine

RUN mkdir -p /srv/app
WORKDIR /srv/app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=$PYTHONPATH:/srv/app

ADD requirements.txt /srv/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ADD . /srv/app

EXPOSE 8500
CMD python3 prev.py
