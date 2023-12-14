【aws system manager】基本機能と活用方法
aws,ssm,system_manager
aws_ssm_basic_functions_and_utilization

## 【aws system manager】基本機能と活用方法

こんにちは。今回は、awsについて初心者エンジニアに向けて、aws system manager（ssm）の基本機能と活用方法について解説します。

### システムマネージャーの概要と利点

aws system manager（ssm）は、awsリソースの管理、監視、自動化を行うためのサービスです。主な利点としては、以下のようなものがあります。

- **簡単なセットアップ**: セットアップは簡単で、aws cliやawsマネジメントコンソールから直感的に操作することができます。
- **一元的な管理**: ssmを使用することで、複数のawsリソース（ec2インスタンス、オンプレミスサーバー、オンプレミスvmなど）を一元的に管理できます。
- **リモートアクセスとリモートコマンド実行**: aws ssmを活用すると、リモートでサーバーにアクセスし、コマンドを実行することが可能です。
- **セキュアなアクセス制御**: iamポリシーを使用して、ユーザーごとに必要な権限を制御することができます。

### インスタンス管理と自動化の手法

ssmを活用することで、ec2インスタンスの管理と自動化を行うことができます。以下に一例を示します。

1. **インスタンスの設定**: ssmを使用して、ec2インスタンスの各種設定を行うことができます。例えば、インスタンスに特定のパッケージや設定ファイルをインストールする場合に、ssmのrun commandを使用してコマンドを実行できます。

```bash
aws ssm send-command --instance-ids i-1234567890abcdefg --document-name "aws-runshellscript" --parameters commands=["apt-get update","apt-get install -y nginx"]
```

2. **パラメータストアの利用**: ssmのパラメータストアを活用することで、機密情報や設定値を暗号化して管理することができます。これにより、インスタンス上でのパスワードやapiキーの直接的な記述を回避し、セキュリティを強化することができます。

```bash
aws ssm put-parameter --name "/myapp/db_username" --value "myusername" --type "securestring"
```

3. **診断と監視**: ssmのrun commandを使用して、ec2インスタンス上での診断を行うことができます。例えば、インスタンス内のログファイルの確認や特定のプロセスのステータスの確認を自動化することができます。

```bash
aws ssm send-command --instance-ids i-1234567890abcdefg --document-name "aws-runpowershellscript" --parameters commands=["get-content c:\logs\app.log"]
```

### パッチ管理とセキュリティのベストプラクティス

aws ssmは、パッチ管理とセキュリティのベストプラクティスを実現するための強力なツールです。以下に一例を示します。

1. **パッチ自動適用**: ssmを使用してec2インスタンスのパッチを自動的に適用することができます。ssmのパッチ管理機能を活用することで、手動でのパッチ適用作業が不要となり、セキュリティと可用性を向上させることができます。

```bash
aws ssm create-patch-baseline --name "mypatchbaseline" --operating-system "amazon_linux_2" --approved-patches-compliance-level "critical"
aws ssm create-association --name "mypatchassociation" --instance-id "i-1234567890abcdefg" --patch-baseline "arn:aws:ssm:us-east-1:123456789012:patchbaseline/mypatchbaseline" --approved-patches "all"
```

2. **セキュリティ情報の収集**: ssmのrun commandを使用して、ec2インスタンスのセキュリティ情報を収集することができます。例えば、インスタンス内のセキュリティグループの設定を確認することで、潜在的なセキュリティ上の脆弱性を特定することができます。

```bash
aws ssm send-command --instance-ids i-1234567890abcdefg --document-name "aws-runshellscript" --parameters commands=["aws ec2 describe-security-groups --group-ids sg-12345678"]
```

### セッションマネージャーの活用法とセキュアなリモートアクセス

aws ssmのセッションマネージャーを活用することで、セキュアなリモートアクセスを実現することができます。以下に一例を示します。

1. **インスタンスへのリモートアクセス**: ssmのセッションマネージャーを使用すると、ec2インスタンスに対して必要な権限を持つユーザーがブラウザ上でリモートアクセスできます。このため、sshキーを共有する必要がなく、セキュリティリスクが軽減されます。

```bash
aws ssm start-session --target i-1234567890abcdefg
```

2. **セキュリティグループの管理**: ssmのセッションマネージャーを使用して、ec2インスタンスのセキュリティグループの設定を変更することができます。例えば、特定のipアドレスからのアクセスを制限する場合に、ssmのrun commandを使用してセキュリティグループのルールを変更できます。

```bash
aws ssm send-command --instance-ids i-1234567890abcdefg --document-name "aws-updatesecuritygroupruledescriptionsingress" --parameters "groupid: 'sg-12345678',cidr: '192.0.2.0/24',oldruledescriptionprefix: 'allow from '"
```

### カスタムドキュメントとスクリプトの管理

最後に、aws ssmを使用してカスタムドキュメントやスクリプトを管理する方法を紹介します。

1. **カスタムドキュメントの作成と実行**: ssmには、awsが提供するオフィシャルドキュメントだけでなく、独自のカスタムドキュメントを作成して使用することができます。例えば、ec2インスタンスのaws cliバージョンをアップデートするためのカスタムドキュメントを作成し、sshやec2 run commandを使わずにバージョンアップすることができます。

```bash
aws ssm create-document --content "<script>\n#!/bin/bash\nsudo pip install awscli --upgrade\n</script>" --name "mycustomdocument" --document-type "command"
aws ssm send-command --instance-ids i-1234567890abcdefg --document-name "mycustomdocument"
```

2. **スクリプトの自動実行**: ssmを使用して、ec2インスタンス上で定期的にスクリプトを実行することができます。例えば、セキュリティパッチの適用状況を定期的にチェックするスクリプトを作成し、ssmのautomationを使用して自動実行できます。

```bash
aws ssm create-automation --document-name "aws-applysecurityupdates" --parameters "{\"instanceid\":[\"i-1234567890abcdefg\"]}"
```

以上が、aws system manager（ssm）の基本機能と活用方法についての解説でした。ssmを活用することで、awsリソースの管理と運用を効率化し、セキュリティと可用性を向上させることができます。是非、これらの機能を試してみてください。

参考記事：
- [【aws再入門】ssm(session manager)を使ってec2インスタンスにsshログインする方法](https://dev.classmethod.jp/articles/aws-session-manager/)
- [aws systems manager のセキュリティについて（前編：iamポリシー）](https://aws.amazon.com/jp/blogs/news/securing-aws-systems-manager-state-manager-with-iam-policies-part-1/)

　

## 【AWS System Manager】関連のまとめ
https://hack-note.com/summary/aws-ssm-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

