【aws system manager】クラウドウォッチログとアラート設定
aws,ssm,system_manager
aws_ssm_cloudwatch_logs_and_alert_configuration

## 【aws system manager】クラウドウォッチログとアラート設定

こんにちは。今回は、awsについて初心者エンジニア向けに、aws ssm（system manager）を使ったクラウドウォッチログの収集とアラート設定について解説します。

### クラウドウォッチログの概要と活用シナリオ

aws cloudwatchは、リソースやアプリケーションのパフォーマンス監視やトラブルシューティングのためのモニタリングサービスです。その中でもクラウドウォッチログは、aws上で発生したログデータを収集・監視するためのサービスです。ログデータはリージョンやアカウントをまたがって収集できるため、さまざまなアプリケーションやサービスのログを一元管理することができます。

クラウドウォッチログを活用することで、以下のようなシナリオに対応することが可能です。

- エラーログの収集: アプリケーションやサーバーのエラーログを収集し、問題の特定や解決に役立てることができます。
- 監査ログの収集: セキュリティ対策やコンプライアンス要件を満たすために、特定のアクションやイベントのログを収集することができます。
- パフォーマンスモニタリング: システムの負荷やパフォーマンスに関するログを収集し、トラブルシューティングや最適化のための分析を行うことができます。

詳細情報は、以下の記事を参考にしてください。

- [aws cloudwatch ログとアラートのモニタリング](https://aws.amazon.com/jp/cloudwatch/features/?nc1=h_ls)
- [aws cloudwatch logs ガイド](https://docs.aws.amazon.com/ja_jp/amazoncloudwatch/latest/logs/whatiscloudwatchlogs.html)

### クラウドウォッチログの収集と設定手順

クラウドウォッチログを収集するためには、aws ssm（systems manager）を使用します。ssmは、awsリソース上での運用・管理タスクを自動化するための統合管理サービスです。

具体的な手順は以下の通りです。

1. aws マネジメントコンソールにログインし、aws ssm のページに移動します。
2. クラウドウォッチログを収集したい ec2 インスタンスを選択します。
3. actions メニューから「create association」を選択します。
4. ドキュメントのタイプとして `aws-configurecloudwatch` を選択し、必要なパラメーターを入力します。
   ```md
   ```
5. ドキュメント名に `cloudwatchlogsconfiguration` など適切な名前を付け、実行をクリックします。

詳細な手順は、以下の記事を参考にしてください。

- [aws ssm（systems manager）ドキュメント](https://docs.aws.amazon.com/ja_jp/systems-manager/latest/userguide/ssm-docs.html)
- [ec2 インスタンスへの systems manager のアクセスと自動フォールバックの設定](https://aws.amazon.com/jp/blogs/news/how-to-ensure-business-continuity-during-failure-of-ssh-keys-on-amazon-ec2-instances-by-using-aws-systems-manager/)

### アラートルールの作成とトリガー設定

クラウドウォッチログを監視するためには、アラートルールを作成し、必要なイベントが発生した際に通知を受けることができます。アラートルールは、「マトリックス式」や「パターン式」を使用して、ログデータから条件にマッチするログイベントを検出します。

アラートルールの作成手順は以下の通りです。

1. aws マネジメントコンソールにログインし、cloudwatch ダッシュボードに移動します。
2. アラームを作成するためのメトリクスとしてクラウドウォッチログを選択します。
3. トリガー条件として適切なマトリックス式やパターン式を設定します。
   ```md
   ```
4. 通知先として、sns トピックや lambda 関数を選択します。

詳細な手順は、以下の記事を参考にしてください。

- [amazon cloudwatch アラームの作成と設定](https://docs.aws.amazon.com/ja_jp/amazoncloudwatch/latest/monitoring/alarmthatsendsemail.html)

### ログデータの分析と異常検知方法

クラウドウォッチログでは、収集したログデータを分析し、異常を検知することができます。異常検知に効果的なのがメトリクスフィルター機能であり、ログデータから必要な情報を抽出してメトリクス化することができます。

メトリクスフィルターの設定手順は以下の通りです。

1. aws マネジメントコンソールにログインし、cloudwatch ダッシュボードに移動します。
2. メトリクスフィルターを作成するためのロググループを選択します。
3. メトリクスフィルターの作成を選択し、適切なフィルターパターンを定義します。
   ```md
   ```
4. メトリクスの設定を行い、必要な場合はアラートルールやダッシュボードへの追加も行います。

詳細な手順は、以下の記事を参考にしてください。

- [cloudwatch メトリクスフィルタを使用してログデータをメトリクス化する](https://docs.aws.amazon.com/ja_jp/amazoncloudwatch/latest/logs/filterandpatternsyntax.html)

### アラート通知のカスタマイズとレポート作成

クラウドウォッチログのアラート通知は、sns トピックや lambda 関数を使ってカスタマイズすることができます。また、定期的なレポートの作成やダッシュボードの設計も行うことができます。

アラート通知のカスタマイズ手順は以下の通りです。

1. aws マネジメントコンソールにログインし、cloudwatch ダッシュボードに移動します。
2. 通知の設定を作成または編集します。
3. カスタマイズした通知先として、sns トピックや lambda 関数を指定します。

レポート作成の手順は以下の通りです。

1. aws マネジメントコンソールにログインし、cloudwatch ダッシュボードに移動します。
2. ダッシュボードを設定し、必要なグラフやメトリクスを追加します。
3. レポートの作成を選択し、ダッシュボードの設定に基づいてレポートを作成します。

詳細な手順は、以下の記事を参考にしてください。

- [amazon cloudwatch アラートのカスタムアクション](https://docs.aws.amazon.com/ja_jp/amazoncloudwatch/latest/monitoring/us_setupsns.html)
- [cloudwatch ダッシュボードについて](https://docs.aws.amazon.com/ja_jp/amazoncloudwatch/latest/monitoring/cloudwatch_dashboards.html)

以上が、aws ssmを使用してクラウドウォッチログの収集とアラート設定を行うための手順となります。クラウドウォッチログを活用することで、アプリケーションやサーバーの監視、トラブルシューティング、セキュリティ対策などを効果的に行うことができます。初心者の方でも手軽に設定できるので、ぜひ試してみてください。

　

## 【AWS System Manager】関連のまとめ
https://hack-note.com/summary/aws-ssm-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

