【aws system manager】セッションマネージャーの活用法
aws,ssm,system_manager
aws_ssm_session_manager_utilization

## 【aws system manager】セッションマネージャーの活用法

こんにちは。今回は、awsについて初心者エンジニアに向けて、aws system managerのセッションマネージャーの活用法についてご紹介します。

## セッションマネージャーの概要と利点
aws system managerのセッションマネージャーは、awsリソースへの安全で迅速なアクセスを提供するためのマネージドサービスです。セッションマネージャーを使用することで、sshやリモートデスクトップ(rdp)などのプロトコルを使用せずに、awsリソースへのリモートセッションを確立できます。

セッションマネージャーの利点は以下の通りです。

1. セキュアなリモートアクセス: セッションマネージャーは、セッション用のプロキシサーバーを介して通信を行うため、sshやrdpのようなプロトコルを利用しないため、安全性が向上します。

2. インスタンスidベースのアクセス: セッションマネージャーは、インスタンスのidを指定してリモートセッションを確立するため、特定のec2インスタンスに対してのみアクセスすることができます。

3. インフラストラクチャーリソースの集中管理: セッションマネージャーを使用することで、リモートアクセスのためのパブリックipアドレスやセキュリティグループの設定をする必要がなくなります。

これらの利点を活かして、セッションマネージャーを使用した便利な活用法を見ていきましょう。

## セッションマネージャーのセキュアなリモートアクセス手法
セッションマネージャーを使用することで、セキュアなリモートアクセスを実現することができます。セッションマネージャーを利用するためには、以下の手順を実行します。

1. iamロールの作成: セッションマネージャーを使用するためには、iamロールの作成が必要です。iamロールには`amazonssmmanagedinstancecore`のポリシーを付与し、ec2インスタンスにロールを割り当てます。

2. セッションマネージャープラグインのインストール: ec2インスタンスにssmエージェントをインストールし、セッションマネージャープラグインを有効にします。

3. セッションマネージャーの利用: awsマネジメントコンソールまたはaws cliからセッションマネージャーのセッションを開始することができます。セッションを開始するには、対象のec2インスタンスのidを指定するだけで簡単にアクセスすることができます。

以下にaws cliを使用してセッションマネージャーを開始するサンプルコードを示します。

```bash
aws ssm start-session --target i-1234567890abcdef0
```

## セッションマネージャーを使用したインスタンスのトラブルシューティング
セッションマネージャーは、インスタンスのトラブルシューティングに非常に便利です。セッションマネージャーを使用することで、リモートアクセスを必要とせずにインスタンスのログや状態を確認することができます。

以下に、セッションマネージャーを使用してインスタンスのトラブルシューティングを行うサンプルコードを示します。

```bash
aws ssm describe-instance-information --instance-information-filter-list "key=instancestatus,values=failed"
```

## セッションマネージャーと統合されたコマンド実行とスクリプトの管理
セッションマネージャーは、インスタンスへのリモートコマンド実行やスクリプトの管理にも活用することができます。セッションマネージャーを使用することで、リモートコマンドを実行するためのssh接続の設定や、スクリプトの転送・実行の手間を省くことができます。

以下に、セッションマネージャーを使用してコマンド実行とスクリプトの管理を行うサンプルコードを示します。

```bash
aws ssm send-command --instance-ids i-12345 --document-name "aws-runshellscript" --parameters 'commands=["ls -al"]'
```

```bash
aws ssm create-association --name "myscriptassociation" --targets "key=instanceids,values=i-12345" --document-version "$default" --parameters 'commands=curl -sl https://example.com/somescript.sh | bash'
```

## セッションマネージャーのロギングと監査機能
セッションマネージャーは、実行されたセッションやコマンドのログを保存することができます。また、cloudwatch logsにログを転送することも可能です。これにより、セッションやコマンドの実行状況を確認し、セキュリティおよび監査要件を満たすことができます。

以下に、セッションマネージャーのログを保存する設定例を示します。

```bash
aws ssm update-association-status --name "myscriptassociation" --output-location "s3bucket=my-log-bucket,s3prefix=ssm-logs"
```

以上が、aws system managerのセッションマネージャーの活用法についての紹介でした。セッションマネージャーを活用することで、セキュアなリモートアクセスやインスタンスのトラブルシューティング、コマンド実行やスクリプト管理、ログの保存といった様々な活用が可能です。

参考記事：
1. [aws systems manager: セッションマネージャーを使用して ec2 インスタンスに対してセキュリティリモートアクセスを可能にする](https://aws.amazon.com/jp/blogs/news/enabling-secure-remote-access-to-ec2-instances-using-aws-systems-manager-session-manager/)
2. [aws systems manager セッションマネージャーを使ってみる](https://qiita.com/hiraku/items/800fab3a6edbcad606a4)

　

## 【AWS System Manager】関連のまとめ
https://hack-note.com/summary/aws-ssm-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

