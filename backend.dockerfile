FROM python:3.7
LABEL maintainer="Valon Januzaj <valon.januzaj98@gmail.com>"

WORKDIR /app
ENV FLASK_APP app/app.py
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY app/requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .
