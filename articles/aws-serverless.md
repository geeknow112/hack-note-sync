AWSサーバーレス入門：はじめの1歩の手順
AWS,サーバーレス
aws-serverless

こんにちは。今回は、AWSについて初心者エンジニア向けに、サーバーレスについて解説します。近年、サーバーレスは注目されており、AWSでもLambdaなどのサーバーレスサービスが提供されています。この記事では、サーバーレスの基礎から、AWSでのサーバーレス開発に必要な知識やサンプルコードを紹介していきます。

## サーバーレスとは

サーバーレスとは、従来のサーバーを必要としないアプリケーション開発手法のことです。つまり、サーバーの管理やインフラストラクチャの設定などが不要となり、開発者はコードの実装に専念することができます。AWSでは、LambdaやAPI Gateway、DynamoDBなど、多くのサーバーレスサービスが提供されています。

サーバーレスのメリットは、以下の通りです。

- サーバーの管理や運用コストが不要
- インフラストラクチャのスケーリングが自動化され、負荷に応じて自動的にサーバーを起動・停止するため、コスト削減につながる
- マイクロサービス化が容易になるため、アプリケーションの開発が迅速になる
- ファンクション単位で課金されるため、細かい粒度でコストを管理できる

ただし、サーバーレスには以下のような課題もあります。

- ファンクションの起動に時間がかかるため、リアルタイム性の高いアプリケーションでは不向き
- インフラストラクチャの管理がAWSに依存するため、AWSが障害を起こした場合にはアプリケーションも影響を受ける
- 複雑なアプリケーションになると、ファンクション間の連携が難しくなることがある

## サーバーレスの基本概念

### Lambda

Lambdaは、AWSのサーバーレスサービスの一つで、コードを実行するためのサービスです。Lambdaは、以下のような特徴があります。

- インフラストラクチャの管理が不要
- マイクロサービス化が容易
- イベント駆動型のアプリケーション開発が可能

Lambdaで実行されるコードは、Java、Python、Node.jsなどのプログラミング言語に対応しています。Lambdaは、API GatewayやDynamoDBなどのAWSサービスと連携することができます。

### API Gateway

API Gatewayは、LambdaなどのAWSサーバーレスサービスを外部から呼び出すためのサービスです。API Gatewayは、以下のような特徴があります。

- サーバーの管理が不要
- RESTful APIの作成が容易
- APIキーによるアクセス制御が可能

API Gatewayは、Lambdaの実行に必要なパラメータを受け取り、Lambdaの実行結果を返す役割を持っています。

### DynamoDB

DynamoDBは、AWSのマネージド型NoSQLデータベースです。DynamoDBは、以下のような特徴があります。

- スケーラビリティが高く、負荷に応じて自動的にスケールアップ・ダウンする
- セキュリティ設定が容易
- データベース管理が不要

DynamoDBは、LambdaなどのAWSサーバーレスサービスから容易にアクセスすることができます。

## サーバーレス開発の手順

AWSでのサーバーレス開発の手順は、以下の通りです。

1. AWSのアカウントを作成する
2. 必要なサービスを有効化する
3. Lambda関数を作成する
4. API Gatewayを作成する
5. Lambda関数とAPI Gatewayを連携する
6. DynamoDBを作成する
7. Lambda関数とDynamoDBを連携する

手順は簡単ですが、AWSに慣れていない場合は、手順がわかりにくいことがあります。ここでは、手順を具体的に解説します。

### 1. AWSのアカウントを作成する

AWSを利用するためには、AWSのアカウントが必要です。アカウント作成には、クレジットカードの登録が必要となります。アカウント作成後、AWSのコンソールにログインすることができます。

### 2. 必要なサービスを有効化する

LambdaやAPI Gateway、DynamoDBなどのサーバーレスサービスを利用するためには、それらのサービスを有効化する必要があります。コンソールからサービスを有効化することができます。

### 3. Lambda関数を作成する

Lambda関数を作成するためには、Lambdaのコンソールから関数を作成することができます。関数の名前や実行するコード、トリガーなどを設定することができます。

以下は、Pythonで実装されたLambda関数のサンプルコードです。

```python
import json

def lambda_handler(event, context):
    body = {
        "message": "Hello, World!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
```

### 4. API Gatewayを作成する

API Gatewayを作成するためには、API GatewayのコンソールからAPIを作成することができます。APIの名前やエンドポイント、Lambda関数の実行設定などを設定することができます。

### 5. Lambda関数とAPI Gatewayを連携する

Lambda関数とAPI Gatewayを連携するためには、API GatewayのコンソールからLambda関数を選択し、API Gatewayとの統合を設定することができます。

以下は、API GatewayとLambda関数を連携するためのサンプルコードです。

```yaml
swagger: "2.0"
info:
  title: "Sample API"
  version: "1.0.0"
basePath: "/prod"
schemes:
  - "https"
paths:
  /hello:
    get:
      responses:
        '200':
          description: "A simple example API"
          schema:
            type: "object"
            properties:
              message:
                type: "string"
      x-amazon-apigateway-integration:
        uri: "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:HelloWorld/invocations"
        passthroughBehavior: "when_no_match"
        httpMethod: "POST"
        type:
```

　

## AWS 関連のまとめ
https://hack-note.com/summary/aws-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

