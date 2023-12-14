【apache】let's encryptのssl証明書を導入する方法
apache,virtualhost,aws,lightsail,let's_encrypt,ssl
apache_ssl_letsencrypt

## let's encryptとは？ssl証明書の基本とメリット

let's encryptは、無料で利用できるssl証明書を提供するプラットフォームです。ssl証明書は、ウェブサイトとユーザー間の通信を暗号化するために使用されます。これにより、ユーザーの個人情報や機密データが盗まれるリスクを軽減することができます。

ssl証明書を使用することの主なメリットは以下の通りです。

1. データの暗号化: ssl証明書により、ウェブサイトとユーザー間の通信が暗号化されます。これにより、第三者が通信内容を傍受しても読むことができません。
2. 権威の証明: ssl証明書は、ウェブサイトが正規の識別情報を持っていることを証明します。ユーザーは、ウェブサイトが信頼できるかどうかを確認するために、ssl証明書の存在を確認することができます。
3. 検索エンジンのランキング向上: googleなどの検索エンジンは、httpsが利用されているウェブサイトを優先的に表示する傾向があります。つまり、ssl証明書を導入することによって、ウェブサイトの検索順位を向上させることができます。

これらの理由により、ssl証明書はウェブサイトにおけるセキュリティと信頼性の向上に欠かせないものとなっています。

参考ブログ記事：
- [let's encryptとssl証明書のメリットとは？ | ベリサインジャパン](https://www.verysign.net/about-lets-encrypt/)
- [ネットワークにおける暗号化とセキュリティについて | google cloud](https://cloud.google.com/security/encryption-in-transit/?hl=ja)

## certbotを使用したlet's encryptのssl証明書の取得手順

certbotは、let's encryptのssl証明書を自動的に取得するためのツールです。certbotを使用することで、手動で証明書を取得する手間を省くことができます。

certbotを使用してlet's encryptのssl証明書を取得する手順は以下の通りです。

```bash
## certbotのインストール（ubuntuの場合）
$ sudo apt-get update
$ sudo apt-get install certbot

## ssl証明書の取得
$ sudo certbot certonly --webroot -w /var/www/example.com -d example.com -d www.example.com

## 証明書の自動更新を設定
$ sudo certbot renew --dry-run
```

以上の手順に従うことで、certbotを使用してlet's encryptのssl証明書を取得し、自動更新も設定することができます。

参考ブログ記事：
- [certbot - クイックスタート | let's encrypt](https://letsencrypt.org/ja/getting-started/)

## apacheでlet's encryptのssl証明書を設定する方法

apacheでlet's encryptのssl証明書を設定するには、以下の手順を実行する必要があります。

1. apacheの設定ファイルを編集して、ssl証明書の場所を指定します。

```bash
## apacheの設定ファイルを編集
$ sudo vi /etc/apache2/sites-available/example.com.conf

## ssl証明書の場所を指定
<virtualhost *:443>
    servername example.com
    documentroot /var/www/example.com

    sslengine on
    sslcertificatefile /etc/letsencrypt/live/example.com/cert.pem
    sslcertificatekeyfile /etc/letsencrypt/live/example.com/privkey.pem
    sslcertificatechainfile /etc/letsencrypt/live/example.com/chain.pem

    ...
</virtualhost>
```

2. apacheを再起動して設定を反映させます。

```bash
## apacheの再起動
$ sudo systemctl restart apache2
```

以上の手順に従うことで、apacheでlet's encryptのssl証明書を設定することができます。

参考ブログ記事：
- [let's encryptの証明書をapacheで使う方法 | qiita](https://qiita.com/eternalamateur/items/c7ef48a8e3ec16452bd9)

## ssl証明書の自動更新と期限切れの管理手法

let's encryptのssl証明書は、有効期限が90日間と比較的短いです。そのため、証明書の自動更新と期限切れの管理は重要な作業です。

certbotを使用して証明書の自動更新を設定する手順は以下の通りです。

1. certbotの自動更新スクリプトを作成します。

```bash
$ sudo vi /etc/cron.d/certbot
```

2. 自動更新スクリプトに以下の内容を記述します。

```bash
0 0,12 * * * root test -x /usr/bin/certbot -a \! -d /run/systemd/system && perl -e 'sleep int(rand(43200))' && certbot -q renew
```

3. スクリプトの権限を変更して、自動更新が実行されるようにします。

```bash
$ sudo chmod 755 /etc/cron.d/certbot
```

以上の手順に従うことで、certbotを使用して証明書の自動更新を設定することができます。

また、証明書の期限切れを管理するためには、定期的な証明書の確認が必要です。certbotには、コマンド `certbot certificates` を使用して証明書の有効期限を確認することができます。

参考ブログ記事：
- [certbot - 自動更新 | let's encrypt](https://letsencrypt.org/ja/docs/using.html#renewal)
- [let's encryptの証明書を自動更新する | qiita](https://qiita.com/noraworld/items/c84c2f04446315819c95)

## let's encryptのssl証明書を確認する方法とhttps接続のテスト

let's encryptのssl証明書が正しく設定されているかどうかを確認するには、以下の手順を実行します。

1. `https://example.com` など、ウェブブラウザでhttpsでアクセスします。
2. アドレスバーに緑色の鍵アイコンが表示され、ウェブサイトの正当性が確認されたことを示すことを確認します。

https接続のテストを行う際には、以下のツールを使用することができます。

- [ssl server test (powered by qualys ssl labs)](https://www.ssllabs.com/ssltest/analyze.html)

このツールにウェブサイトのurlを入力することで、ssl証明書の正当性や暗号スイート、プロトコルの使用などを評価することができます。

参考ブログ記事：
- [ブラウザで実際にssl証明書の動作を確認する方法 | ネットワールド](https://networkworld.jp/ns/blog/57540)

　

## 【Apache】関連のまとめ
https://hack-note.com/summary/apache-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

