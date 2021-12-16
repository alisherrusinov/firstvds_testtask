FROM python:3.8

WORKDIR /usr/src/app

RUN pip install --upgrade pip setuptools wheel

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .