#!/bin/bash

cd "$(dirname "$0")"
source .venv/bin/activate
exec gunicorn -b unix:/tmp/testbank.sock -w1 testbank.wsgi
