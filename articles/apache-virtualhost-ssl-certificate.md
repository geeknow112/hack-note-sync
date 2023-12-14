【apache】仮想ホストのセキュリティ強化：ssl証明書を使用する方法
apache,virtualhost
apache-virtualhost-ssl-certificate

## ssl証明書の入手とインストール手順

### 何がssl証明書だ？
まずはじめに、ssl証明書が何なのかを簡単に説明します。ssl証明書は、ウェブサイトと訪問者の間の通信を暗号化するための仕組みです。証明書には、ウェブサイトのドメイン名や組織名、発行元などの情報が含まれています。これにより、訪問者はウェブサイトが信頼できるものであることを確認することができます。

### ssl証明書の入手方法
ssl証明書を入手する方法はいくつかありますが、ここではlet's encryptという無料の証明書発行機関を利用した方法を紹介します。

let's encryptを使用するには、まずcertbotというツールをインストールする必要があります。certbotは、let's encryptとの通信を管理するためのクライアントです。

```bash
$ sudo apt-get update
$ sudo apt-get install certbot
```

certbotをインストールしたら、以下のコマンドを実行してssl証明書の取得を行います。

```bash
$ sudo certbot certonly --webroot -w /var/www/example -d example.com -d www.example.com
```

上記のコマンドでは、`/var/www/example` 以下にウェブサイトのファイルが存在することを前提としています。適切なパスに置き換えてください。

ssl証明書の取得に成功すると、`/etc/letsencrypt/live/example.com/` ディレクトリに証明書のファイルが保存されます。

### ssl証明書のインストール方法
次に、取得したssl証明書をapacheの仮想ホストにインストールします。

まずは、証明書の鍵ファイル（privkey.pem）と証明書ファイル（fullchain.pem）を仮想ホストの設定ファイルに指定します。

```apache
<virtualhost *:443>
    documentroot /var/www/example
    servername example.com
    sslengine on
    sslcertificatefile /etc/letsencrypt/live/example.com/fullchain.pem
    sslcertificatekeyfile /etc/letsencrypt/live/example.com/privkey.pem
</virtualhost>
```

上記の設定では、`example.com` というドメインの証明書を使用することを指定しています。適切なドメイン名に置き換えてください。

設定を保存したら、apacheを再起動して変更を反映させます。

```bash
$ sudo service apache2 restart
```

これで、ウェブサイトの仮想ホストにssl証明書が適用されました。

参考url：
- [certbot](https://certbot.eff.org/)
- [let's encrypt](https://letsencrypt.org/)


## apacheでのsslモジュールの有効化方法

### apacheのsslモジュールとは
apacheはデフォルトではssl（secure sockets layer）モジュールが無効化されています。sslを使用するためには、このモジュールを有効化する必要があります。

### sslモジュールの有効化
まずはじめに、sshでサーバに接続して、以下のコマンドを実行します。

```bash
$ sudo a2enmod ssl
```

上記のコマンドを実行すると、sslモジュールが有効化されます。その後、apacheを再起動して変更を反映させます。

```bash
$ sudo service apache2 restart
```

これで、apacheでsslを使用する準備が整いました。

参考url：
- [apache ssl/tls encryption](http://httpd.apache.org/docs/current/ssl/ssl_howto.html)


## httpsリダイレクトの設定とhttpからの自動転送

### httpsリダイレクトとは
httpsリダイレクトは、ウェブサイトへのアクセスをhttpからhttpsに自動的に転送する仕組みです。これにより、ウェブサイトのセキュリティが向上し、訪問者のプライバシーが保護されます。

### httpsリダイレクトの設定
httpsリダイレクトを設定するには、apacheの設定ファイルに以下の記述を追加します。

```apache
<virtualhost *:80>
    servername example.com
    redirect permanent / https://example.com/
</virtualhost>

<virtualhost *:443>
    documentroot /var/www/example
    servername example.com
    sslengine on
    sslcertificatefile /etc/letsencrypt/live/example.com/fullchain.pem
    sslcertificatekeyfile /etc/letsencrypt/live/example.com/privkey.pem
</virtualhost>
```

上記の設定では、ポート80（http）へのアクセスがあった場合に、httpsへのリダイレクトが行われます。

設定を保存したら、apacheを再起動して変更を反映させます。

```bash
$ sudo service apache2 restart
```

これで、httpからのアクセスが自動的にhttpsへ転送されるようになりました。

参考url：
- [redirecting http to https in apache](https://www.namecheap.com/support/knowledgebase/article.aspx/9821/33/redirecting-http-to-https-in-apache)


## sslプロトコルと暗号スイートの設定と最適化

### sslプロトコルと暗号スイート
sslプロトコルと暗号スイートは、通信の暗号化とセキュリティを担保するために使用されます。

### sslプロトコルと暗号スイートの設定
apacheの設定ファイルに以下の記述を追加することで、sslプロトコルと暗号スイートの設定を行うことができます。

```apache
<virtualhost *:443>
    documentroot /var/www/example
    servername example.com
    sslengine on
    sslcertificatefile /etc/letsencrypt/live/example.com/fullchain.pem
    sslcertificatekeyfile /etc/letsencrypt/live/example.com/privkey.pem

    sslprotocol -all +tlsv1.2
    sslciphersuite eecdh+aesgcm:edh+aesgcm:aes256+eecdh:aes256+edh
</virtualhost>
```

上記の設定では、tlsv1.2プロトコルのみを有効化し、暗号スイートにはaesgcmとaes256を使用するように指定しています。

設定を保存したら、apacheを再起動して変更を反映させます。

```bash
$ sudo service apache2 restart
```

これで、ウェブサイトの通信はより安全な暗号化方式で行われるようになりました。

参考url：
- [ssl protocol and cipher suite](https://httpd.apache.org/docs/2.4/mod/mod_ssl.html#sslprotocol)
- [cipher suite names](https://httpd.apache.org/docs/2.4/mod/mod_ssl.html#ciphersuite)


## ssl証明書の更新と期限切れの管理手法

### ssl証明書の更新
ssl証明書は一定期間ごとに更新する必要があります。証明書の有効期限が切れる前に更新することで、ウェブサイトのセキュリティを継続的に保つことができます。

ssl証明書の更新は、certbotを使用して行います。以下のコマンドを実行することで、証明書の更新を行うことができます。

```bash
$ sudo certbot renew
```

このコマンドを定期的に実行することで、自動的にssl証明書の更新が行われます。

### 期限切れの管理
証明書の有効期限が切れた場合、ウェブサイトのセキュリティが脆弱になるため、適切な管理が必要です。

証明書の有効期限が近づくと、certbotは通知を送信する機能があります。これにより、証明書の更新が必要なことを事前に知ることができます。

また、証明書が期限切れになった場合には、新たな証明書を取得して適用する必要があります。証明書の有効期限が切れたことに気づいたら、すぐに更新作業を行うようにしましょう。

参考url：
- [certbot user guide](https://certbot.eff.org/docs/using.html#renewing-certificates)

　

## 【Apache】関連のまとめ
https://hack-note.com/summary/apache-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

