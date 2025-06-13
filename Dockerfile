FROM python:3.11-slim

WORKDIR /app
COPY . /app

# 先にビルドに必要なOSパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
