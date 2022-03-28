FROM python:3.8
ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY . /code

RUN python -m pip install -r requirements.txt

EXPOSE 8000