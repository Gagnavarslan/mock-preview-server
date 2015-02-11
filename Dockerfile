FROM python:2.7
MAINTAINER Axel Örn Sigurðsson <axel@absalon.is>

ADD . /opt/preview
WORKDIR /opt/preview
EXPOSE 8500

RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py
RUN python /tmp/get-pip.py

RUN pip install -r requirements.txt

ENTRYPOINT python prev.py
