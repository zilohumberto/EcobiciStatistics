from ubuntu:16.04

LABEL Creator: "Humberto Felipe Rodriguez Rodriguez"

RUN apt update -y

# Install dependencies
RUN apt-get update && apt-get install -yq --no-install-recommends python3 python3-virtualenv

RUN apt install -yq  python3-pip

RUN mkdir /home/ecobici/

RUN mkdir /home/ecobici/output/

RUN mkdir /home/ecobici/output/error_process

RUN mkdir /home/ecobici/output/ok_process

RUN mkdir /home/ecobici/output/EXTERNAL_SOURCE

ENV PYTHONPATH /home/ecobici

COPY dev-requirements.txt /

RUN pip3 install -r /dev-requirements.txt

RUN cd /home/ecobici/

CMD ["python3","/home/ecobici/core/translator/folder_watcher.py"]


