【apache】virtualhostとlet's encryptを使ったssl証明書の自動更新方法
apache,virtualhost,aws,lightsail,let's_encrypt,ssl
apache_virtualhost_ssl_auto_renewal

## 【apache】virtualhostとlet's encryptを使ったssl証明書の自動更新方法

こんにちは。今回は、apacheについて初心者エンジニアに向けて、virtualhostとlet's encryptを使ったssl証明書の自動更新方法について解説します。

## let's encryptと自動更新：ssl証明書の重要性とメリット

ssl証明書は、ウェブサイトのセキュリティを確保するために必要なものです。特に個人情報の取り扱いやパスワードの送信など、信頼性を求められるサイトでは、ssl証明書を使用することが推奨されています。

let's encryptは、無料で使用できるオープンソースのssl証明書発行機関です。一般的には、証明書の有効期限は90日間となっており、期限が切れるたびに手動で証明書を更新する必要があります。しかし、let's encryptを使えば、証明書の自動更新を設定することができます。

証明書の自動更新にはいくつかの方法がありますが、今回はcertbotというツールを使用して設定します。

## certbotを使用した自動更新の設定手順

### ステップ1：certbotのインストール

まずは、certbotをインストールします。certbotは、各osによってインストール方法が異なるので、以下の公式ドキュメントを参考にインストールしてください。

[https://certbot.eff.org/instructions](https://certbot.eff.org/instructions)

### ステップ2：certbotによる証明書の発行と自動更新の設定

インストールが完了したら、次に証明書の発行と自動更新の設定を行います。

以下のコマンドを使用して、certbotを実行します。

```
sudo certbot certonly --webroot -w /var/www/html -d example.com
```

上記のコマンドでは、webrootを/var/www/htmlに指定してexample.comというドメインの証明書を発行しています。適宜自分の環境に合わせて設定してください。

証明書の発行が完了すると、certbotは自動更新用の設定ファイルを生成します。これにより、証明書の更新を自動化することができます。

### ステップ3：apache virtualhostの設定

証明書が発行されたら、次はapache virtualhostの設定を行います。virtualhostは、複数のドメインやサブドメインを同一サーバー上で運用するための仕組みです。

以下のような設定を行います。

```
<virtualhost *:443>
    servername example.com
    documentroot /var/www/html/example.com
    sslengine on
    sslcertificatefile /etc/letsencrypt/live/example.com/fullchain.pem
    sslcertificatekeyfile /etc/letsencrypt/live/example.com/privkey.pem
</virtualhost>
```

上記の例では、example.comというドメインに対してssl証明書を適用する設定を行っています。適宜自分の環境に合わせて設定してください。

## apache virtualhostの確認と設定の自動化

apache virtualhostの設定が正しく行われているか確認するために、以下のコマンドを使用します。

```
sudo apache2ctl -t
```

エラーがなければ、設定は問題ありません。

設定の自動化を行うためには、証明書の自動更新とapacheの再起動を定期的に行う必要があります。そのためには、クーロンジョブを使用すると便利です。

## クーロンジョブを使った定期的な自動更新のスケジューリング

クーロンジョブを使って定期的に証明書の自動更新とapacheの再起動を行うためには、以下のステップを実行します。

1. クーロンジョブの編集
```
crontab -e
```

2. クーロンジョブの追加
以下のコマンドを追記します。
```
0 0 * * 0 certbot renew --quiet && /etc/init.d/apache2 restart
```

上記のクーロンジョブは、毎週日曜日の0時にcertbotを実行し、証明書を更新してからapacheを再起動します。

## 自動更新の監視とエラーハンドリング：更新失敗時の対処方法

証明書の自動更新では、更新に失敗することもあります。失敗した場合に備えて、自動更新の監視とエラーハンドリングが必要です。

以下のスクリプトを作成し、失敗時に通知するようにします。

```bash
#!/bin/bash

/usr/bin/certbot renew --quiet || /path/to/send_notification_script.sh
```

上記のスクリプトでは、certbotの自動更新を試行し、更新に失敗した場合にsend_notification_script.shを実行します。send_notification_script.shは、通知を行うスクリプトです。

以上で、apacheのvirtualhostとlet's encryptを使ったssl証明書の自動更新方法の解説を終わります。証明書の有効期限切れの問題から解放され、常に安全な状態でウェブサイトを運営できるようになります。

参考記事:
- [https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-20-04)
- [https://tecadmin.net/letsencrypt-auto-renew-certbot-os-labels/](https://tecadmin.net/letsencrypt-auto-renew-certbot-os-labels/)

　

## 【Apache】関連のまとめ
https://hack-note.com/summary/apache-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)


