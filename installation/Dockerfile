from ubuntu:16.04

LABEL Creator: "Humberto Felipe Rodriguez Rodriguez"

RUN apt update -y

# Install dependencies
RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

RUN apt install -y  python3-pip -y

RUN mkdir /home/ecobici/

RUN mkdir /home/ecobici/output/

RUN mkdir /home/ecobici/output/error_process

RUN mkdir /home/ecobici/output/ok_process

RUN mkdir /home/ecobici/output/EXTERNAL_SOURCE

ENV PYTHONPATH /home/ecobici

RUN python3 -m virtualenv --python=/usr/bin/python3 /opt/venv

COPY dev-requirements.txt .

RUN . /opt/venv/bin/activate && pip install -r dev-requirements.txt

RUN cd /home/ecobici/

CMD . /opt/venv/bin/activate

