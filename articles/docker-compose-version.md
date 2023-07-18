Docker Composeで簡単に複数コンテナを管理しよう
Docker,Docker-Compose
docker-compose-version

こんにちは。今回は、Docker初心者に向けて、Docker Composeについて解説します。Docker Composeは、複数のDockerコンテナを定義し、一括で管理するためのツールです。複数のコンテナを一つひとつ手動で起動するのは手間がかかるため、Docker Composeを使うことで効率的にコンテナを管理できます。

## Docker Composeとは

Docker Composeは、Dockerコンテナを定義し、起動・停止・再起動などを一括で管理するためのツールです。Docker Composeの設定ファイル（docker-compose.yml）に必要な情報を記述することで、複数のコンテナを一括で管理することができます。

## Docker Composeのインストール

Docker Composeは、Dockerと同様に公式サイトからダウンロードすることができます。以下のコマンドを実行することで、最新版のDocker Composeがダウンロードされます。

```bash
$ sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

ダウンロードが完了したら、以下のコマンドを実行してDocker Composeを実行可能にします。

```bash
$ sudo chmod +x /usr/local/bin/docker-compose
```

正しくインストールされたかどうかを確認するために、以下のコマンドを実行してバージョン情報を確認します。

```bash
$ docker-compose --version
```

## Docker Composeの設定ファイル

Docker Composeの設定ファイルは、YAML形式で記述されます。設定ファイルの名前はデフォルトで「docker-compose.yml」となっていますが、任意の名前をつけることもできます。

設定ファイルでは、複数のサービス（＝コンテナ）を定義します。以下は、WordPressとMySQLをDocker Composeで管理するための設定ファイルの例です。

```yaml
version: '3'

services:
  db:
    image: mysql:5.7
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress

  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    ports:
      - "8000:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress

volumes:
  db_data:
```

この設定ファイルでは、MySQLとWordPressのコンテナを定義しています。MySQLコンテナでは、データを永続化するためのボリュームを定義し、WordPressコンテナでは、MySQLコンテナに依存していることを定義しています。また、WordPressコンテナのポート番号を8000に設定しています。

## Docker Composeの基本的なコマンド

Docker Composeの基本的なコマンドを紹介します。

### Docker Composeの起動

Docker Composeの設定ファイルを元に、コンテナを起動するには以下のコマンドを実行します。

```bash
$ docker-compose up
```

### Docker Composeの停止

Docker Composeで起動したコンテナを停止するには以下のコマンドを実行します。

```bash
$ docker-compose down
```

### Docker Composeの再起動

Docker Composeで起動したコンテナを再起動するには以下のコマンドを実行します。

```bash
$ docker-compose restart
```

## サンプルコード

以下は、Docker Composeを使ってFlaskアプリケーションを起動するための設定ファイルの例です。

```yaml
version: '3'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
    environment:
      FLASK_APP: app.py
      FLASK_ENV: development
    command: flask run --host=0.0.0.0
```

この設定ファイルでは、Flaskアプリケーションを起動するためのコンテナを定義しています。Dockerfileを使ってイメージをビルドし、ポート番号5000番でアプリケーションを公開しています。また、アプリケーションのコードをボリュームとしてマウントしています。

```Dockerfile
FROM python:3.9

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
```

Flaskアプリケーションのコードは以下の通りです。

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

## 注意点

Docker Composeを使ってコンテナを管理する際には、以下の点に注意する必要があります。

- コンテナ間の依存関係を正しく定義すること
- ポート番号の競合に注意すること
- コンテナのリソース制限に注意すること

以上が、Docker Composeについての基本的な解説です。複数のコンテナを一括で管理することで、Dockerの効率的な利用ができます。Docker Composeを使って、簡単に複数のコンテナを管理してみてください。

　

## Docker 関連のまとめ
https://hack-note.com/summary/docker-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

