【aws cli】cloudformationスタックの作成と更新
aws,cli
aws_cli_cloudformation

## aws cliを使用したcloudformationスタックの作成手順

aws cliを使ってcloudformationスタックを作成する手順をご紹介します。aws cliは、ターミナルやコマンドプロンプトからawsの各種サービスを操作するためのコマンドツールです。以下の手順に従って、cloudformationスタックを作成しましょう。

### 1. aws cliのインストール

まず最初に、aws cliをインストールします。aws cliはpythonのパッケージとして提供されており、以下のコマンドでインストールすることができます。

```
$ pip install awscli
```

インストールが完了したら、以下のコマンドでaws cliのバージョンを確認してみましょう。

```
$ aws --version
```

### 2. aws cliの設定

aws cliを使うためには、awsのアクセスキーとシークレットアクセスキーが必要です。これらの情報を設定するために、以下のコマンドを実行します。

```
$ aws configure
```

実行すると、awsアカウントのアクセスキー、シークレットアクセスキー、デフォルトのリージョン、出力形式などを入力するように求められます。適切な情報を入力してください。

### 3. cloudformationテンプレートの作成

次に、cloudformationテンプレートを作成します。cloudformationテンプレートは、スタックの構成情報やリソースの定義を記述するjsonまたはyaml形式のファイルです。以下のコマンドで、テンプレートファイルを作成しましょう。

```
$ touch template.yml
```

作成したテンプレートファイルに、cloudformationスタックの構成情報やリソースの定義を記述してください。具体的な記述方法については、awsの公式ドキュメントや以下のブログ記事を参考にしてください。

- [aws公式ドキュメント: aws cloudformation ユーザーガイド](https://docs.aws.amazon.com/ja_jp/awscloudformation/latest/userguide/welcome.html)
- [qiita: aws cloudformationでvpc & ec2インスタンスを構築する](https://qiita.com/ka-/items/df62de57fd5bfa7e686e)

### 4. cloudformationスタックの作成

cloudformationテンプレートが完成したら、以下のコマンドでスタックを作成します。

```
$ aws cloudformation create-stack --stack-name my-stack --template-body file://template.yml
```

上記のコマンドでは、スタックの名前を`my-stack`とし、テンプレートファイルのパスを指定しています。適宜、スタック名やテンプレートファイルのパスを変更して実行してください。

### 5. cloudformationスタックの状態の確認

スタックの作成が開始されたら、以下のコマンドでスタックの状態を確認することができます。

```
$ aws cloudformation describe-stacks --stack-name my-stack
```

スタックの状態は、`create_in_progress`、`create_complete`、`create_failed`などのいずれかの値で表されます。

以上で、aws cliを使用したcloudformationスタックの作成手順を紹介しました。次は、cloudformationテンプレートの作成とパラメータの設定方法について説明します。

## cloudformationテンプレートの作成とパラメータの設定方法

cloudformationテンプレートは、スタックの構成情報やリソースの定義を記述するjsonまたはyaml形式のファイルです。cloudformationテンプレートの作成方法と、パラメータの設定方法について説明します。

### テンプレートファイルの記述

cloudformationテンプレートは、jsonまたはyaml形式で記述することができます。以下に、json形式でのテンプレートファイルの記述例を示します。

```json
{
  "awstemplateformatversion": "2010-09-09",
  "description": "my cloudformation stack",
  "resources": {
    "myec2instance": {
      "type": "aws::ec2::instance",
      "properties": {
        "imageid": "ami-0c94855ba95c71c99",
        "instancetype": "t2.micro"
      }
    }
  }
}
```

上記の例では、`myec2instance`という名前のec2インスタンスを作成しています。インスタンスのami idやインスタンスタイプなどのプロパティを指定することができます。具体的なリソースタイプやプロパティの指定方法については、awsの公式ドキュメントや参考記事を参考にしてください。

### パラメータの設定

cloudformationテンプレートでは、スタック作成時にパラメータを指定することができます。例えば、スタック作成時に指定するリソース名やパスワードなどの値をパラメータとして受け取ることができます。

パラメータは、テンプレートファイル内の`parameters`セクションで指定します。以下に、パラメータを指定したテンプレートファイルの記述例を示します。

```json
{
  "awstemplateformatversion": "2010-09-09",
  "description": "my cloudformation stack",
  "parameters": {
    "instancename": {
      "type": "string",
      "default": "myinstance"
    }
  },
  "resources": {
    "myec2instance": {
      "type": "aws::ec2::instance",
      "properties": {
        "imageid": "ami-0c94855ba95c71c99",
        "instancetype": "t2.micro",
        "tags": [
          {
            "key": "name",
            "value": { "ref": "instancename" }
          }
        ]
      }
    }
  }
}
```

上記の例では、`instancename`というパラメータを指定しています。パラメータの値は、スタック作成時に指定することができます。また、テンプレート内のリソース定義でパラメータの値を使う場合は`{ "ref": "パラメータ名" }`という形式で指定します。

以上で、cloudformationテンプレートの作成とパラメータの設定方法について説明しました。次は、aws cliでのcloudformationスタックの更新と変更セットの適用方法について説明します。

## aws cliでのcloudformationスタックの更新と変更セットの適用

cloudformationスタックを作成した後も、スタックの内容を更新することができます。aws cliを使ってcloudformationスタックを更新し、変更セットを適用する手順を説明します。

### cloudformationスタックの更新

cloudformationスタックを更新するには、まず変更内容を反映した新しいテンプレートファイルを作成します。変更内容に応じて、テンプレートファイルの適切な箇所を修正してください。

次に、以下のコマンドでcloudformationスタックを更新します。

```
$ aws cloudformation update-stack --stack-name my-stack --template-body file://template.yml
```

上記のコマンドでは、`my-stack`という名前のスタックを更新し、新しいテンプレートファイルを指定しています。スタック名やテンプレートファイルのパスは適宜変更してください。

### 変更セットの作成と適用

cloudformationスタックを更新する際には、変更内容の詳細を確認してから適用させることができます。変更セットを作成することで、変更内容をスタックに適用する前に確認することができます。

変更セットを作成するには、以下のコマンドを実行します。

```
$ aws cloudformation create-change-set --stack-name my-stack --template-body file://template.yml --change-set-name my-change-set
```

上記のコマンドでは、`my-change-set`という名前の変更セットを作成しています。スタック名やテンプレートファイルのパスは適宜変更してください。

変更セットを作成した後は、変更内容を確認することができます。以下のコマンドで変更内容を詳細に表示させることができます。

```
$ aws cloudformation describe-change-set --change-set-name my-change-set
```

変更内容を確認し、問題がなければ以下のコマンドで変更セットを適用させます。

```
$ aws cloudformation execute-change-set --change-set-name my-change-set
```

以上で、aws cliでのcloudformationスタックの更新と変更セットの適用方法について説明しました。次は、cloudformationスタックのステータスの監視とロールバック処理について説明します。

## cloudformationスタックのステータスの監視とロールバック処理

cloudformationスタックの作成や更新時には、スタックのステータスを監視することが重要です。スタックのステータスには、`create_in_progress`、`create_complete`、`create_failed`などの値があります。

スタックのステータスを監視するには、以下のコマンドを使用します。

```
$ aws cloudformation describe-stack-events --stack-name my-stack
```

上記のコマンドでは、`my-stack`という名前のスタックの変更イベントを表示します。スタックの作成や更新時には、変更イベントのログを確認することで進捗状況やエラーの原因を特定することができます。

また、スタックの作成や更新に失敗した場合には、ロールバック処理を行うことができます。ロールバック処理を行うには、以下のコマンドを実行します。

```
$ aws cloudformation delete-stack --stack-name my-stack
```

上記のコマンドでは、`my-stack`という名前のスタックを削除することでロールバックを行っています。スタックの削除によって、変更を適用する前の状態にスタックを戻すことができます。

以上で、cloudformationスタックのステータスの監視とロールバック処理について説明しました。最後に、aws cliを使ったcloudformationスタックの削除とリソースのクリーンアップ方法について紹介します。

## aws cliを使ったcloudformationスタックの削除とリソースのクリーンアップ方法

cloudformationスタックの削除とリソースのクリーンアップについて説明します。aws cliを使用してスタックを削除することで、スタックが作成したリソースも同時に削除されます。

### cloudformationスタックの削除

cloudformationスタックを削除するには、以下のコマンドを実行します。

```
$ aws cloudformation delete-stack --stack-name my-stack
```

上記のコマンドでは、`my-stack`という名前のスタックを削除します。スタック名は適宜変更してください。

### リソースのクリーンアップ

スタックの削除によってスタックが作成したリソースが削除されますが、一部のリソースは明示的な削除処理が必要となる場合があります。例えば、s3バケットやrdsインスタンスなどです。

これらのリソースは、以下のコマンドで個別に削除することができます。

```
$ aws s3 rm s3://my-bucket --recursive
```

上記のコマンドでは、`my-bucket`という名前のs3バケットを再帰的に削除しています。s3バケットの名前や削除するリソースに合わせて適宜変更してください。

以上で、aws cliを使ったcloudformationスタックの削除とリソースのクリーンアップ方法について説明しました。初心者エンジニアの方にとって、aws cliを使ったcloudformationスタックの作成や更新は初めての経験かもしれませんが、この記事を参考にしてスムーズに操作することができるはずです。awsの公式ドキュメントや参考記事も併せて活用しながら、aws cliをマスターしてください。

　

## 【aws cli】関連のまとめ
https://hack-note.com/summary/aws-cli-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

