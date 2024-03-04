#!/bin/bash

set -o errexit
set -o nounset

if [[ "${1}" == "celery" ]]; then
  celery --app=core.celery.base:celery worker --loglevel=info
elif [[ "${1}" == "flower" ]]; then
  celery --app=core.celery.base:celery flower
fi