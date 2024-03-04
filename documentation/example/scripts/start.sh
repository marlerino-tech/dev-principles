#!/bin/bash

alembic upgrade head

gunicorn core.server:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT