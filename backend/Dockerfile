FROM python:3.8

MAINTAINER Chris Josh "christopherjoshua25@hotmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /zenoContainer/backend

COPY requirements.txt /zenoContainer/backend

RUN pip install -r requirements.txt

COPY . /zenoContainer/backend

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

