【基礎】AWS lightsailで無料SSLを設定する方法
aws,lightsail,無料,手順
aws-lightsail-free-ssl

こんにちは。今回は、awsについて初心者エンジニアに向けて、aws lightsailで無料sslを設定する方法について解説します。

## aws lightsail 無料sslとは？

aws lightsailは、awsのクラウドインフラストラクチャを使って、配信ネットワーク、データベース、ストレージなどを簡単にセットアップして使えるようにしたサービスです。また、sslについても無料の証明書を提供しています。

## aws lightsailで無料sslを使わない場合の選択肢

無料sslを使わない場合、ユーザーがウェブサイトにアクセスする際に警告メッセージが表示され、セキュリティに対して不信感を持たれる可能性があります。

また、sslを使わない場合、盗聴や改竄、なりすましなどの攻撃リスクが高まるため、セキュリティリスクが増します。

## aws lightsailで無料sslを設定する手順

1. aws lightsailのコンソールにログインし、lightsailのダッシュボードを開きます。
2. ネットワーキングから、ロードバランサーを選択します。
3. ロードバランサーの設定画面を開き、証明書の追加ボタンをクリックします。
4. ssl証明書設定画面が開くので、amazon配布証明書を選択します。
5. 追加するドメイン名を入力します。
6. amazon配布証明書を有効にするために、lightsailアカウントidをaws certificate managerに登録する必要があります。登録後、証明書発行をクリックします。
7. 証明書が追加され、ロードバランサーの設定が更新されます。
8. ドメインを独自ドメインに変更する場合は、dnsレコードを変更する必要があります。

## 注意点

証明書の更新については、aws certificate managerに登録するメールアドレスに通知が届きます。期限が迫っている場合は、必ず更新作業を行ってください。

また、無料sslは1年ごとに更新する必要があります。期限が切れる前に更新作業を行っておくことが重要です。

以上が、aws lightsailで無料sslを設定する手順となります。

>注意点をしっかりと確認し、定期的な更新作業を行うことが重要です。

参考記事：
- [aws lightsailでssl有料版から無料版設定](https://qiita.com/ohtaman/items/88b11fcc011f8fd4248a)
- [aws lightsail、amazon linux 2、letsencryptで無料ssl設定](https://qiita.com/chanpionjeff/items/460f25a75ea49cbb492e)

　

## AWS Lightsail 関連のまとめ
https://hack-note.com/summary/aws-lightsail-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)


