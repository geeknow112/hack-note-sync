【aws cli】基本コマンドと使い方
aws,cli
aws_cli_basics

## aws cliの基本コマンドと使い方

こんにちは。今回は、aws cliについて初心者エンジニアに向けて、基本的なコマンドと使い方について解説します。aws cli（command line interface）は、コマンドラインからawsのリソースを管理するためのツールであり、guiではできない高度な操作やスクリプトの自動化などに利用されます。

### aws cliのインストールと環境設定

まず、aws cliを利用するためには、事前にインストールと環境設定が必要です。以下の手順に従って、aws cliをインストールし、環境設定を行いましょう。

1. aws cliのインストール

aws cliのインストールは、各osに合わせたパッケージマネージャーを使用する方法や、公式のインストーラーを利用する方法などがあります。詳細なインストール手順は、以下の公式ドキュメントを参照してください。

- [aws cliのインストール（公式ドキュメント）](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-configure-files.html)

2. aws cliの環境設定

インストールが完了したら、次にaws cliの環境設定を行います。以下のコマンドを実行して、awsのアクセスキーとシークレットキーを設定しましょう。

```
$ aws configure
aws access key id [none]: <アクセスキーを入力>
aws secret access key [none]: <シークレットキーを入力>
default region name [none]: <デフォルトのリージョンを入力>
default output format [none]: <出力形式を入力（例：json）>
```

aws cliの環境設定が完了したら、次に基本的なコマンドの使い方を学んでいきましょう。

### aws cliでの認証情報の設定方法

aws cliでは、コンソール上で手動で設定する以外にも、環境変数やプロファイル、iamロールなどを使用して認証情報を設定することもできます。以下では、基本的な認証情報の設定方法について解説します。

1. 環境変数を使用した設定

環境変数を使用してaws cliの認証情報を設定するには、以下のように環境変数を設定します。

```
$ export aws_access_key_id=<アクセスキー>
$ export aws_secret_access_key=<シークレットキー>
$ export aws_default_region=<リージョン>
```

2. プロファイルを使用した設定

プロファイルを使用してaws cliの認証情報を設定するには、awsのクレデンシャルファイル (credentials) と設定ファイル (config) を編集します。詳細な設定方法は、以下の公式ドキュメントを参照してください。

- [aws cliの認証情報の設定（公式ドキュメント）](https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-configure-files.html)

### aws cliでのリージョンの指定と切り替え

aws cliでは、デフォルトのリージョン以外にも別のリージョンを指定または切り替えることができます。以下では、リージョンの指定方法と切り替え方法について解説します。

1. リージョンの指定

aws cliでリソースを作成する場合、デフォルトのリージョンが使用されます。しかし、作成したいリソースを異なるリージョンに作成したい場合は、以下のコマンドでリージョンを指定することができます。

```
$ aws configure set region <リージョン>
```

2. リージョンの切り替え

既に指定したデフォルトのリージョンがある場合、別のリージョンに切り替えたい場合は、以下のコマンドでリージョンを切り替えることができます。

```
$ export aws_default_region=<リージョン>
```

以上で、aws cliでのリージョンの指定と切り替えの方法について説明しました。

### aws cliでのコマンドの構文とオプションの解説

aws cliでは、各種のリソースを操作するためのコマンドが用意されています。それぞれのコマンドの構文やオプションについて理解することが重要です。以下では、aws cliのコマンドの構文とオプションについて解説します。

1. コマンドの構文

aws cliのコマンドの構文は、一般的な形式を持っています。以下は一般的な構文の例です。

```
$ aws <service> <command> <subcommand> [--key1 value1] [--key2 value2] ...
```

- `<service>`: awsの各種サービス名（例: ec2, s3, lambda）
- `<command>`: サービスの操作コマンド（例: create, delete, describe）
- `<subcommand>`: サービスの操作対象を指定するコマンド（例: instance, bucket, function）
- `[--key1 value1] [--key2 value2] ...`: オプションやパラメータを指定する部分

2. オプションの解説

aws cliのコマンドには、様々なオプションが存在します。オプションには省略可能なものや必須のものがあり、コマンドによって異なります。以下は一般的なオプションの例です。

- `--version` オプション: aws cliのバージョンを表示する
- `--profile` オプション: プロファイルを指定して認証情報を使用する
- `--region` オプション: リージョンを指定する
- `--output` オプション: 出力形式を指定する（例: json, text）

以上で、aws cliでのコマンドの構文とオプションについて解説しました。

### aws cliを使ったリソースの作成と管理

最後に、aws cliを使ってリソースを作成および管理する方法について解説します。以下では、一般的なリソースでの使用例を示します。

1. ec2インスタンスの作成

以下のコマンドを使用して、指定したパラメータに基づいてec2インスタンスを作成します。

```
$ aws ec2 run-instances --image-id <ami_id> --instance-type <instance_type> --key-name <key_pair_name> --security-group-ids <security_group_id> --subnet-id <subnet_id>
```

2. s3バケットの作成

以下のコマンドを使用して、指定したバケット名でs3バケットを作成します。

```
$ aws s3 mb s3://<bucket_name>
```

3. lambda関数の作成

以下のコマンドを使用して、指定したパラメータに基づいてlambda関数を作成します。

```
$ aws lambda create-function --function-name <function_name> --runtime <runtime> --role <role_arn> --handler <handler_function>
```

以上で、aws cliを使ったリソースの作成と管理の方法について解説しました。

まとめると、今回はaws cliについて初心者エンジニア向けに、基本的なコマンドと使い方について解説しました。aws cliのインストールと環境設定、認証情報の設定方法、リージョンの指定と切り替え、コマンドの構文とオプションの解説、リソースの作成と管理について学びました。aws cliは自動化や高度な操作に役立つツールであり、awsのリソースを効率的に管理するために活用しましょう。

参考記事：
- [aws cli（aws コマンドライン インターフェイス）の使い方を解説！](https://liginc.co.jp/490193)
- [aws cliの使い方入門【初心者向け】](https://dev.classmethod.jp/articles/aws-cli-introduction/)

　

## 【AWS CLI】関連のまとめ
https://hack-note.com/summary/aws-cli-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

