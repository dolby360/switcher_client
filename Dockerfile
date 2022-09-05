FROM python:3.10.6-slim-buster
WORKDIR /usr/src/app
RUN apt update && apt upgrade -y && apt install iputils-ping -y
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .