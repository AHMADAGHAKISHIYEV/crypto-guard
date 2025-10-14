FROM python:3.11-slim

WORKDIR /worker

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY worker/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY api /worker/api
COPY worker/worker.py ./worker.py
COPY worker/tasks ./tasks

ENV PYTHONPATH=/worker

CMD ["celery", "-A", "worker:celery_app", "worker", "--loglevel=info"]
