【aws system manager】インスタンス管理とモニタリング
aws,ssm,system_manager
aws_ssm_instance_management_and_monitoring

## インスタンス管理の基本と重要な機能

### aws systems managerとは

aws systems manager（以下、ssm）は、awsのクラウドリソースを効率的に管理するためのサービスです。ssmを使用することで、インフラストラクチャの設定管理やパフォーマンスのモニタリング、インスタンスへのアクセス制御などを行うことができます。

### ssmのインスタンス管理機能

ssmを使用することで、インスタンスの管理を行うことができます。ssmのインスタンス管理機能には以下のようなものがあります。

#### インスタンスへのリモートアクセス

ssmを使用することで、sshやrdpのようなリモートアクセスのためのポートをオープンする必要がありません。代わりに、awsマネジメントコンソールやaws cliを使用して、インスタンスに直接アクセスすることができます。

```bash
# aws cliを使用したインスタンスへのリモートアクセス
aws ssm start-session --target instance-id
```

#### インスタンスのパッチ管理

ssmを使用することで、インスタンスのパッチ適用を自動化することができます。パッチ適用のスケジュール設定やパッチの種類を指定することで、自動的にパッチを適用することができます。

```yaml
# パッチマネージャの設定
resourcetype: "aws::ssm::patchbaseline"
properties:
  name: "samplepatchbaseline"
  operatingsystem: "windows"
  approvalrules:
    patchrules:
      - patchfiltergroup:
          patchfilters:
            - key: product
              values:
                - "windowsserver2016"
      - compliancelevel: "critical"
```

#### インスタンスの設定管理

ssmを使用することで、インスタンスの設定管理を行うことができます。設定ファイルの配布や設定変更、プロセスの監視などが可能です。

```bash
# インスタンスにssm agentをインストールするコマンド例
aws ssm create-instance-information --region ap-northeast-1 --instance-id i-xxxxxxx

# インスタンスの設定を指定してコマンドを実行する例
aws ssm send-command --document-name "aws-runshellscript" --targets "key=tag:environment,values=test" --parameters commands=ls --region ap-northeast-1
```

## インスタンスの自動デプロイとスケーリング

### aws codedeployとの統合

ssmは、aws codedeployとの統合により、インスタンスの自動デプロイを行うことができます。codedeployを使用することで、アプリケーションのデプロイプロセスを自動化し、デプロイの成功率を向上させることができます。

```yaml
# codedeployのデプロイグループの設定例
resources:
  myec2instance:
    type: "aws::ec2::instance"
    properties:
      instancetype: !ref instancetype
      imageid: ami-xxxxxxxx
  mydeploymentgroup:
    type: "aws::codedeploy::deploymentgroup"
    properties:
      applicationname: !ref codedeployapplication
      deploymentgroupname: "mydeploymentgroup"
      deploymentconfigname: "codedeploydefault.oneatatime"
      servicerolearn: !ref codedeployservicerole
      autoscalinggroups:
        - !ref myautoscalinggroup
      ec2tagset:
        ec2tagsetlist:
          - ec2taggroup:
              - key: "name"
                value: "myec2instance"
              - key: "environment"
                value: "production"
          - ec2taggroup:
              - key: "name"
                value: "myec2instance"
              - key: "environment"
                value: "staging"
```

### インスタンスのスケーリング

ssmは、インスタンスのスケーリングにも活用することができます。auto scalingグループによるインスタンスの起動や終了など、スケーリングに関する操作を自動化することができます。

```bash
# auto scalingグループの作成
aws autoscaling create-auto-scaling-group --auto-scaling-group-name example-group --instance-id i-xxxxxxx --min-size 2 --max-size 10

# インスタンスのスケールアウト
aws ssm send-command --document-name "aws-runshellscript" --targets "key=tag:environment,values=test" --parameters commands="aws autoscaling set-desired-capacity --auto-scaling-group-name example-group --desired-capacity 4" --region ap-northeast-1
```

## インスタンスパフォーマンスのモニタリングと最適化

### イベントベースのインスタンスモニタリング

ssmは、インスタンスのパフォーマンス監視やエラー検出のためのイベントベースのモニタリングを提供しています。cloudwatchやcloudtrailなどのawsサービスとの統合により、インスタンスの状態やアラートなどをリアルタイムに監視することができます。

```bash
# インスタンスのリソース利用率のモニタリング
aws ssm send-command --document-name "aws-runshellscript" --targets "key=tag:name,values=ec2instance" --parameters commands="sar -u 1 10" --region ap-northeast-1
```

### インスタンスの最適化

ssmを使用することで、インスタンスの最適な設定や構成変更を行うことができます。インスタンスのリソース利用率やボトルネックの検出、パフォーマンスの改善策などを提案することができます。

```bash
# インスタンスのリソース利用状況の収集
aws ssm send-command --document-name "aws-runshellscript" --targets "instanceids=i-xxxxxxx" --parameters commands="top -bn1" --region ap-northeast-1

# ユーザーデータを指定してインスタンスにパフォーマンスの最適化を実施する
aws ec2 run-instances --image-id ami-xxxxxxx --instance-type t3.large --key-name mykeypair --user-data file://configure-instance.sh
```

## インスタンスのログ収集と分析手法

### インスタンスログの収集

ssmを使用することで、インスタンスのログ収集を行うことができます。cloudtrailなどのawsサービスとの統合により、インスタンスのログをリアルタイムで収集することができます。

```bash
# インスタンスのログの取得と表示
aws ssm start-session --target instance-id
cat /var/log/syslog
```

### インスタンスログの分析手法

ssmを使用することで、インスタンスのログを分析し、問題の特定と解決策の提案を行うことができます。ログの解析や異常検知などの高度な分析手法を活用することで、インスタンスのトラブルシューティングや改善策の立案を行うことができます。

```bash
# cloudwatch logs insightsを使用したログの分析
aws logs start-query --log-group-name myloggroup --query-string 'fields @timestamp, @message | filter @message like /error/ | sort @timestamp desc | limit 10'

# amazon athenaを使用したログのクエリ
aws athena start-query-execution --query-string "select * from mytable where status = 'error'"

# ログのダウンサンプリングと異常検知
aws cloudwatch put-metric-alarm --alarm-name myalarm --metric-name cpuutilization --namespace aws/ec2 --statistic average --period 60 --threshold 80 --comparison-operator greaterthanorequaltothreshold --evaluation-periods 1 --alarm-actions arn:aws:sns:us-west-2:123456789012:mytopic --unit percent
```

## インスタンスのセキュリティとアクセス制御

### セキュリティグループとの統合

ssmを使用することで、セキュリティグループとの統合が可能となります。セキュリティグループのルールやアクセス制御の設定をssmを通じて管理することができます。

```bash
# セキュリティグループの構成情報の表示
aws ssm describe-instance-information --filters "key=tag-key,values=environment" --region ap-northeast-1

# セキュリティグループの追加
aws ssm send-command --document-name "aws-runshellscript" --targets "key=tag:name,values=ec2instance" --parameters commands="aws ec2 authorize-security-group-ingress --group-id sg-xxxxxxxx --protocol tcp --port 22 --source 0.0.0.0/0" --region ap-northeast-1
```

### iamロールとの統合

ssmを使用することで、iamロールとの統合が可能となります。iamロールのポリシーや権限設定をssmを通じて管理することができます。

```bash
# iamロールの作成
aws iam create-role --role-name myrole --assume-role-policy-document file://trust-policy.json

# iamロールにポリシーをアタッチ
aws iam attach-role-policy --role-name myrole --policy-arn arn:aws:iam::123456789012:policy/mypolicy

# ssmによるロールの設定
aws ssm register-default-patch-baseline --baseline-id pb-xxxxxxxx

# インスタンスにiamロールを割り当て
aws ec2 associate-iam-instance-profile --instance-id i-xxxxxxx --iam-instance-profile name=myinstanceprofile
```

## まとめ

今回は、awsのシステムマネージャ（ssm）を使用したインスタンスの管理とモニタリングについて紹介しました。ssmを活用することで、インスタンスの設定管理やパフォーマンスのモニタリング、ログの収集などを効率的に行うことができます。初心者エンジニアでも簡単に利用できるため、awsの運用管理において重要なツールとなります。

参考文献：
- [aws systems manager ドキュメント](https://docs.aws.amazon.com/systems-manager/index.html)
- [aws cli ドキュメント](https://docs.aws.amazon.com/cli/index.html)

　

## 【AWS System Manager】関連のまとめ
https://hack-note.com/summary/aws-ssm-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

