#!/usr/bin/env sh

# Start server.
echo "Starting gunicorn server"
gunicorn --config /code/etc/gunicorn_conf.py wsgi:app