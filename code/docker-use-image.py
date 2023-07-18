## ```Dockerfile
# ベースイメージを指定
FROM python:3.9-slim-buster

# 作業ディレクトリを指定
WORKDIR /app

# アプリケーションの依存関係をインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# アプリケーションをコピー
COPY . .

# アプリケーションを実行
CMD ["python", "app.py"]
## ```


## ```bash
docker build -t my-python-app .
## ```


## ```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
## ```


## ```Dockerfile
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
## ```


## ```bash
docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app
## ```
