# ```Dockerfile
# ベースイメージの指定
FROM イメージ名:タグ

# パッケージのインストールや設定の実行
RUN コマンド1 \
    && コマンド2 \
    && ...

# ポートの公開
EXPOSE ポート番号

# コンテナ実行時に実行されるコマンドの指定
CMD ["コマンド", "引数1", "引数2", ...]
# ```


# ```Dockerfile
FROM python:3.9
# ```


# ```Dockerfile
RUN apt-get update \
    && apt-get install -y git \
    && git clone https://github.com/example/example.git
# ```


# ```Dockerfile
EXPOSE 8000
# ```


# ```Dockerfile
CMD ["python", "app.py"]
# ```


# ```Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
# ```
