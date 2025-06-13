FROM python:3.11-slim

WORKDIR /app
COPY . /app

# PyNaCl のビルドに必要な libffi-dev を先に入れる
RUN apt-get update && apt-get install -y libffi-dev gcc

# pip のアップグレードFROM python:3.11-slim

WORKDIR /app
COPY . /app

# PyNaClに必要なビルドツールや依存をインストール
RUN apt-get update && apt-get install -y \
    libffi-dev \
    libssl-dev \
    build-essential \
    gcc \
    python3-dev

# pipアップグレードとライブラリインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]

RUN pip install --upgrade pip

# ライブラリインストール
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
