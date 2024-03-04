FROM python:3.11-slim-buster as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS python-deps


# Mariadb Depedencies


# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
#RUN useradd --create-home appuser
WORKDIR /backend
#RUN #chown -R appuser:appuser /backend
#RUN #chmod 777 /backend


# Install application into container
COPY ./app ./app
COPY ./core ./core
COPY ./templates ./templates
COPY ./static ./static
COPY ./langs ./langs

COPY ./Makefile .

RUN mkdir -p ./log
RUN mkdir -p ./applications
COPY ./applications/manifest.php ./applications/manifest.php
RUN mkdir -p ./static/img

#USER appuser

EXPOSE 8888
ENTRYPOINT ["gunicorn", "core.server:app"]
CMD ["--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8888"]

