#!/usr/bin/env sh
cd "final project" || exit 1
python -m pip install --upgrade pip
python -m pip install --no-cache-dir gunicorn==20.1.0
python -m gunicorn web_app:app --bind 0.0.0.0:$PORT
