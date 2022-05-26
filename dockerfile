FROM python:slim

RUN pip install pytest pylint flake8 coverage \
    && apt -y update \
    && apt -y install git

WORKDIR /mnt