#!/bin/sh

gunicorn -w 2 -c python:config.gunicorn  app.app:app
