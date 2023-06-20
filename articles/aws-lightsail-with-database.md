AWS Lightsailとデータストアの選択
AWS,Lightsail,RDS,データベース
aws-lightsail-with-database

こんにちは。今回は、AWS Lightsailとデータストアの選択について解説します。

## AWS LightsailとRDSの最安プラン

AWS Lightsailは、AWSのクラウドサービスの中でも手軽に利用できるサービスです。Lightsailでは、データベースとしてMySQLとPostgreSQLをサポートしていますが、RDSを利用する場合には制限があります。

RDSインスタンスは、同じリージョン内にあるLightsailインスタンスからのみ利用可能であり、またRDSインスタンスはLightsailインスタンスと同じVPC内に作成する必要があります。そのため、RDSを利用することが難しい場合があります。

AWS RDSの最も安価なプランは、t3.microインスタンスを利用する「バースト可能な汎用パフォーマンス」プランです。このプランの料金は、AWSの東京リージョンで以下の通りです。

- t3.microインスタンスの場合：0.017 USD/時間
- ストレージ（汎用SSD）：0.115 USD/GB/月
- バックアップ：0.05 USD/GB/月

これらの料金に加えて、データベースエンジンの種類によって追加料金が発生する場合があります。

以下に、AWS CLIを使用して、t3.microインスタンスを作成するコマンドを示します。

```bash
aws rds create-db-instance \
--db-instance-identifier mydbinstance \
--db-instance-class db.t3.micro \
--engine mysql \
--master-username myuser \
--master-user-password mypassword \
--allocated-storage 20 \
--availability-zone ap-northeast-1a \
--db-subnet-group-name mydbsubnetgroup \
--publicly-accessible \
--vpc-security-group-ids mysecuritygroup
```

## AWS Lightsailと他のデータストアの代替案

AWS Lightsail以外にも、データストアとして利用できるAWSのサービスは多数あります。以下に、代表的な代替案を表形式でまとめました。

| 代替案 | 利点 | 欠点 |
| --- | --- | --- |
| Amazon DynamoDB | サーバーレスアーキテクチャーでスケーラビリティが高い | RDBMSとは異なるNoSQLデータベース |
| Amazon Aurora Serverless | サーバーレスアーキテクチャーでスケーラビリティが高い | RDSよりも高価 |
| Amazon DocumentDB | MongoDB互換性があり、スケーラビリティが高い | RDSよりも高価 |
| 自前でのデータベース構築 | 自由度が高く、コストを抑えられる | セキュリティや管理が自己責任となる |

以上が、AWS Lightsailとデータストアの選択についての比較です。用途や予算に応じて適切なデータストアサービスを選択することが重要です。


　

## AWS Lightsail 関連のまとめ
https://hack-note.com/summary/aws-lightsail-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)


