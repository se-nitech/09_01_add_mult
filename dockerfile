FROM python:slim

RUN apt -y update && apt -y install git

WORKDIR /mnt
