【基礎】aws workdocsにバックアップする時の同期について
aws,workdocs
aws-workdocs-sync

こんにちは。今回は、AWSについて初心者エンジニアに向けて、バックアップについてご紹介します。

## aws workdocs にデータをバックアップするには

aws workdocsは、ドキュメント管理サービスであり、エクスポート機能を利用することでデータをバックアップすることができます。エクスポート機能を使えば、全文検索に使われるelasticsearchやamazon s3などにデータをエクスポートすることができます。

## aws workdocs のバックアップしたファイルの同期方法

aws workdocsでバックアップしたファイルは、amazon s3に保存されます。amazon s3は、オブジェクトストレージサービスであり、s3のオブジェクトは、バージョン管理がされます。バックアップしたファイルが同期される際には、バージョン管理の情報を利用して、差分同期が行われます。

## aws workdocs のバックアップの時の差分同期がされる？

aws workdocsでバックアップしたファイルが同期される際には、差分同期が行われます。バージョン管理の情報を利用して、差分を判定し、差分のあるファイルのみ同期が行われます。このため、同じファイルを何度も上書きしても、同期されるのは変更された差分のみになるため、効率的なバックアップが行えます。

>ただし、s3のバージョン管理オプションが有効である必要があります。もしバージョン管理オプションが無効になっている状態でファイルを上書きしてしまうと、上書きされたファイルが最新の状態として同期されてしまい、元のファイルが削除されてしまうことがあります。注意が必要です。

## aws workdocs で継続的にバックアップするには？

aws workdocsのバックアップを自動化するには、aws lambdaを利用して、定期的にバックアップを取得するようにするとよいでしょう。aws lambdaは、サーバーレスのコンピューティングサービスであり、定期的に実行するタスクを設定することができます。バックアップを自動的に取得し、amazon s3に保存するタスクをaws lambdaで実行することで、継続的にバックアップを取得することができます。

ただし、aws lambdaの実行には料金がかかるため、自動化を行う際には必要な予算を準備しておく必要があります。また、aws lambdaの実行回数などによって、料金が変動するため、注意が必要です。使用前によく確認しましょう。

aws workdocsは、データ管理に優れたサービスであり、エクスポート機能を利用して簡単にバックアップを取得することができます。さらに、差分同期が行われるため、効率的にバックアップを行うことができます。定期的にバックアップを取得する場合には、aws lambdaを利用するのがおすすめです。ただし、aws lambdaの使用には注意が必要なため、使用前によく確認しましょう。

参考記事：
- [aws workdocs エクスポート機能を利用してデータを保存する](https://aws.amazon.com/jp/premiumsupport/knowledge-center/workdocs-export-data/)
- [amazon s3 のバージョン管理](https://docs.aws.amazon.com/ja_jp/amazons3/latest/userguide/versioning-what-is-isnot.html)

　

## AWS Workdocs 関連まとめ
https://hack-note.com/summary/aws-workdocs-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

