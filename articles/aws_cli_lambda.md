【aws cli】lambda関数の作成とデプロイ
aws,cli
aws_cli_lambda

## aws cliを使用したlambda関数の作成手順

こんにちは。今回は、aws cliについて初心者エンジニアに向けて、lambda関数の作成とデプロイ方法について解説していきます。

### aws cliとは
aws cli（aws command line interface）は、awsをコマンドラインから操作するためのツールです。guiベースの管理コンソールに比べて、より高度な操作やスクリプトの自動化が可能となります。

まずは、aws cliのインストールから始めましょう。

#### インストール手順

以下の公式ドキュメントを参考に、aws cliをインストールしてください。

[公式ドキュメント](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

インストールが完了したら、次にawsアカウントの設定を行います。

#### awsアカウントの設定

aws cliを使用するためには、awsアカウントのアクセスキーとシークレットアクセスキーが必要です。

以下の公式ドキュメントを参考に、awsアカウントの設定を行ってください。

[公式ドキュメント](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

awsアカウントの設定が完了したら、lambda関数の作成に移りましょう。

#### lambda関数の作成手順

まず、aws cliを使ってlambda関数を作成するために、以下のコマンドを実行してください。

```bash
aws lambda create-function --function-name my-function --runtime python3.7 --role arn:aws:iam::123456789012:role/service-role/lambda-role --handler lambda_function.lambda_handler --zip-file fileb://./function.zip
```

このコマンドでは、以下のパラメータを指定しています。

- `--function-name`：関数の名前を指定します。
- `--runtime`：ランタイム環境を指定します。ここではpython 3.7を使用しています。
- `--role`：iamロールのarnを指定します。
- `--handler`：ハンドラの名前を指定します。
- `--zip-file`：デプロイするzipファイルのパスを指定します。

lambda関数の作成が完了したら、次はlambda関数のコードの作成とデプロイ方法について見ていきましょう。

## lambda関数のコードの作成とデプロイ方法

lambda関数のコードを作成し、デプロイするためには、以下の手順が必要です。

1. 関数のコードを作成する
2. 依存関係を解決する
3. コードをzipファイルに固める
4. 関数をデプロイする

それでは、具体的な手順を見ていきましょう。

### 1. 関数のコードを作成する

まずは、lambda関数のコードを作成しましょう。例として、以下のpythonコードを使います。

```python
import json

def lambda_handler(event, context):
    return {
        'statuscode': 200,
        'body': json.dumps('hello from aws lambda!')
    }
}
```

このコードでは、単純なhttpレスポンスを返すlambda関数を作成しています。

### 2. 依存関係を解決する

もし、関数のコードに依存関係がある場合は、事前にそれらの依存関係を解決しておく必要があります。一般的には、pythonの場合は`pip`を使ってパッケージをインストールします。

```bash
pip install requests
```

### 3. コードをzipファイルに固める

次に、関数のコードをzipファイルに固めましょう。以下のコマンドを使って、zipファイルを作成します。

```bash
zip -r function.zip lambda_function.py
```

このコマンドでは、`lambda_function.py`というファイルをzipファイルに固めています。

### 4. 関数をデプロイする

最後に、作成したzipファイルを使って関数をデプロイします。以下のコマンドを実行してください。

```bash
aws lambda update-function-code --function-name my-function --zip-file fileb://./function.zip
```

このコマンドでは、`--function-name`で関数の名前を指定し、`--zip-file`でデプロイするzipファイルのパスを指定しています。

以上で、lambda関数のコードの作成とデプロイ方法の説明は終わりです。

次は、aws cliでのlambda関数の環境変数と設定の管理について見ていきましょう。

## aws cliでのlambda関数の環境変数と設定の管理

lambda関数の環境変数や設定を管理するためには、aws cliを使用することができます。環境変数や設定をコマンドラインから簡単に操作することができるため、効率的な開発が可能となります。

### 環境変数の設定

まずは、環境変数の設定方法を見ていきましょう。以下のコマンドを使って、環境変数を設定します。

```bash
aws lambda update-function-configuration --function-name my-function --environment variables={key1=value1,key2=value2}
```

このコマンドでは、`--function-name`で関数の名前を指定し、`--environment`で環境変数を指定しています。複数の環境変数を指定する場合は、カンマで区切って指定してください。

### 設定の取得

次に、環境変数や他の設定の値を取得する方法を見ていきましょう。以下のコマンドを使って、設定の値を取得します。

```bash
aws lambda get-function-configuration --function-name my-function
```

このコマンドでは、`--function-name`で関数の名前を指定して設定の値を取得しています。

### 設定の変更

設定の値を変更する場合は、以下のコマンドを使って変更してください。

```bash
aws lambda update-function-configuration --function-name my-function --memory-size 256 --timeout 30
```

このコマンドでは、`--memory-size`でメモリサイズを指定し、`--timeout`でタイムアウト時間を指定しています。

以上で、aws cliでのlambda関数の環境変数と設定の管理の説明は終わりです。

次は、lambda関数のトリガーの設定とイベントソースの統合について見ていきましょう。

## lambda関数のトリガーの設定とイベントソースの統合

lambda関数をトリガーするためには、トリガーの設定とイベントソースの統合が必要です。aws cliを使用することで、トリガーの設定やイベントソースの統合をコマンドラインから簡単に行うことができます。

### トリガーの設定

まずは、トリガーの設定方法を見ていきましょう。以下のコマンドを使って、トリガーを設定します。

```bash
aws lambda create-event-source-mapping --function-name my-function --event-source-arn arn:aws:s3:::my-bucket --batch-size 10 --starting-position latest
```

このコマンドでは、`--function-name`で関数の名前を指定し、`--event-source-arn`でトリガーとなるリソースのarnを指定しています。その他のオプションとして、`--batch-size`でバッチサイズを指定し、`--starting-position`で開始位置を指定します。

### イベントソースの統合

次に、イベントソースの統合方法を見ていきましょう。以下のコマンドを使って、イベントソースを統合します。

```bash
aws lambda create-event-source-mapping --function-name my-function --event-source-arn arn:aws:ses:us-west-2:123456789012:receipt-rule-set/my-rule-set --starting-position latest
```

このコマンドでは、`--function-name`で関数の名前を指定し、`--event-source-arn`でイベントソースのarnを指定しています。イベントソースの統合方法は、トリガーの設定と同様のコマンドを使用します。

以上で、lambda関数のトリガーの設定とイベントソースの統合の説明は終わりです。

次は、aws cliを使ったlambda関数の監視とログの分析について見ていきましょう。

## aws cliを使ったlambda関数の監視とログの分析

lambda関数を監視し、ログを分析するためには、aws cliを使用することができます。aws cliを使って、lambda関数のメトリクスやログの取得、分析が行えます。

### メトリクスの取得

まずは、lambda関数のメトリクスの取得方法を見ていきましょう。以下のコマンドを使って、メトリクスを取得します。

```bash
aws cloudwatch get-metric-statistics --namespace aws/lambda --metric-name invocations --dimensions name=functionname,value=my-function --statistics sum --start-time 2021-01-01t00:00:00z --end-time 2021-01-02t00:00:00z --period 3600
```

このコマンドでは、`--metric-name`でメトリクスの名前を指定し、`--dimensions`で関数名を指定しています。その他のオプションとして、`--statistics`で統計値を指定し、`--start-time`と`--end-time`で取得する期間を指定します。

### ログの取得

次に、lambda関数のログの取得方法を見ていきましょう。以下のコマンドを使って、ログを取得します。

```bash
aws logs filter-log-events --log-group-name /aws/lambda/my-function --start-time 2021-01-01t00:00:00z --end-time 2021-01-02t00:00:00z
```

このコマンドでは、`--log-group-name`でロググループの名前を指定しています。その他のオプションとして、`--start-time`と`--end-time`で取得する期間を指定します。

以上で、aws cliを使ったlambda関数の監視とログの分析の説明は終わりです。

いかがでしたか？aws cliを使用したlambda関数の作成とデプロイ、環境変数や設定の管理、トリガーの設定とイベントソースの統合、監視とログの分析について解説しました。

aws cliは、より高度な操作やスクリプトの自動化が可能となる便利なツールです。ぜひ、活用してみてください。

　

## 【aws cli】関連のまとめ
https://hack-note.com/summary/aws-cli-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

