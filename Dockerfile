FROM python:2.7
MAINTAINER Axel Örn Sigurðsson <axel@absalon.is>

RUN git clone https://github.com/Ikornaselur/mock-preview-server.git /opt/preview

WORKDIR /opt/preview

RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py
RUN python /tmp/get-pip.py

RUN pip install -r requirements.txt

EXPOSE 8500
ENTRYPOINT python prev.py
