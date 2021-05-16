FROM python:3.7-slim-buster as pythonpackages

ENV PYTHONUNBUFFERED 1
WORKDIR /app/backend

RUN apt update -y && apt install -y --no-install-recommends python3 python3-virtualenv build-essential libpq-dev

ENV VIRTUAL_ENV=/opt/env
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY . /app
RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh