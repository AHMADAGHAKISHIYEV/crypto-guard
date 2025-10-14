FROM python:3.11-slim

WORKDIR /bot

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY bot/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY api /bot/api
COPY shared /bot/shared
COPY bot /bot/bot

ENV PYTHONPATH=/bot

CMD ["python", "-m", "bot.bot"]
