【aws cli】セキュリティグループの設定と管理
aws,cli
aws_cli_security_groups

## 【aws cli】セキュリティグループの設定と管理

こんにちは。今回は、aws cliについて初心者エンジニアに向けて、セキュリティグループの設定と管理方法について解説します。

セキュリティグループは、aws上でネットワークトラフィックを管理するための重要な要素です。正しいセキュリティグループの設定と管理ができれば、aws上のインスタンスやサーバーのセキュリティを確保することができます。aws cliを使用することで、コマンドラインでセキュリティグループを作成・設定・監視することができます。

以下では、aws cliを使ったセキュリティグループの作成やルールの設定、変更、削除、適用方法などについて詳しく解説していきます。

## aws cliでのセキュリティグループの作成手順

まずは、aws cliを使ってセキュリティグループを作成する手順について説明します。

```bash
aws ec2 create-security-group --group-name mysecuritygroup --description "my security group" --vpc-id vpc-fb9a3497
```

このコマンドを実行すると、指定したvpc内に"mysecuritygroup"という名前のセキュリティグループが作成されます。descriptionにはセキュリティグループの説明を記述します。

セキュリティグループの作成後、必要なインバウンドルールとアウトバウンドルールをセットする必要があります。

## セキュリティグループのインバウンドルールとアウトバウンドルールの設定

インバウンドルールとアウトバウンドルールは、セキュリティグループに設定される制御ルールです。

以下のコマンドを実行することで、インバウンドルールを追加できます。

```bash
aws ec2 authorize-security-group-ingress --group-name mysecuritygroup --protocol tcp --port 22 --cidr 0.0.0.0/0
```

このコマンドでは、mysecuritygroup というセキュリティグループに対して、tcpプロトコル、ポート番号22、許可元のcidrブロック0.0.0.0/0（全てのipアドレスからの接続を許可）を追加するという設定を行っています。

同様に、アウトバウンドルールを追加するためには、以下のコマンドを実行します。

```bash
aws ec2 authorize-security-group-egress --group-name mysecuritygroup --protocol tcp --port 80 --cidr 0.0.0.0/0
```

このコマンドでは、mysecuritygroup というセキュリティグループに対して、tcpプロトコル、ポート番号80、許可先のcidrブロック0.0.0.0/0（全てのipアドレスへの接続を許可）を追加するという設定を行っています。

## aws cliを使用したセキュリティグループのルールの編集と削除

作成したセキュリティグループのルールを編集したり削除したりするためには、以下のコマンドを使用します。

まず、ルールの編集を行うためには、以下のコマンドを実行します。

```bash
aws ec2 update-security-group-rule-descriptions-ingress --group-name mysecuritygroup --protocol tcp --port 22 --cidr 0.0.0.0/0 --description "updated rule description"
```

このコマンドでは、mysecuritygroup というセキュリティグループのインバウンドルールで、tcpプロトコル、ポート番号22、許可元のcidrブロック0.0.0.0/0に対して、ルールの説明を "updated rule description" に変更します。

また、ルールの削除を行うためには、以下のコマンドを実行します。

```bash
aws ec2 revoke-security-group-ingress --group-name mysecuritygroup --protocol tcp --port 22 --cidr 0.0.0.0/0
```

このコマンドでは、mysecuritygroup というセキュリティグループのインバウンドルールで、tcpプロトコル、ポート番号22、許可元のcidrブロック0.0.0.0/0に対して、ルールを削除します。

## セキュリティグループの適用と関連リソースへの割り当て方法

セキュリティグループを作成した後、ec2インスタンスやrdsインスタンスなどの関連リソースに対して、セキュリティグループを適用する必要があります。

以下のコマンドを使用して、セキュリティグループをec2インスタンスに適用することができます。

```bash
aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --groups sg-01234567890abcdef
```

このコマンドでは、i-1234567890abcdef0 というec2インスタンスに対して、sg-01234567890abcdef というセキュリティグループを適用します。

同様に、rdsインスタンスにセキュリティグループを適用するためには、以下のコマンドを使用します。

```bash
aws rds modify-db-instance --db-instance-identifier mydbinstanceidentifier --vpc-security-group-ids sg-01234567890abcdef
```

このコマンドでは、mydbinstanceidentifier というrdsインスタンスに対して、sg-01234567890abcdef というセキュリティグループを適用します。

## aws cliでのセキュリティグループのロギングと監視

セキュリティグループのログと監視を行うことで、セキュリティインシデントの検知やトラブルシューティングが容易になります。

以下のコマンドを使用して、セキュリティグループのログと監視を有効化することができます。

```bash
aws ec2 create-flow-logs --resource-type vpc --resource-ids vpc-1234567890abcdef0 --traffic-type all --log-group-name myloggroupname --deliver-logs-permission-arn arn:aws:iam::123456789012:role/myflowlogsrole
```

このコマンドでは、vpc-1234567890abcdef0 というvpcに対して、allのトラフィックタイプでのログを作成し、myloggroupname というロググループにログを送信します。さらに、arn:aws:iam::123456789012:role/myflowlogsrole というiamロールを使用してログを配信します。

以上がaws cliを使用してセキュリティグループを設定と管理する方法です。セキュリティグループの適切な設定と管理は、aws上のシステムのセキュリティを確保するうえで非常に重要です。aws cliを使ってセキュリティグループを作成・設定・監視することで、効率的な運用が可能となりますので、ぜひ活用してみてください。

参考記事：
- [aws cli command reference](https://docs.aws.amazon.com/cli/latest/reference/)
- [aws cli documentations](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-index.html)

　

## 【AWS CLI】関連のまとめ
https://hack-note.com/summary/aws-cli-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

