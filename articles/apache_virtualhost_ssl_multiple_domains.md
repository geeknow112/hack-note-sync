【apache】virtualhostを使用して複数ドメインのssl対応サイトを構築する方法
apache,virtualhost,aws,lightsail,let's_encrypt,ssl
apache_virtualhost_ssl_multiple_domains

こんにちは。今回は、
apacheについて初心者エンジニア
に向けて、virtualhostを使用して複数ドメインのssl対応サイトを構築する方法について解説します。

## virtualhostと複数ドメインの関連付け方法
まず、複数のドメインを運用するためには、apacheのvirtualhost機能を利用します。virtualhostは、1つのapacheサーバーで複数のドメインを管理する際に使用される機能であり、それぞれのドメインに対して個別の設定を行うことができます。

以下のような例で、virtualhostの設定を行います。

```apache
<virtualhost *:80>
    servername example.com
    documentroot /var/www/html/example
</virtualhost>

<virtualhost *:80>
    servername example2.com
    documentroot /var/www/html/example2
</virtualhost>
```

上記の例では、example.comとexample2.comという2つのドメインを設定しています。それぞれのドメインに対して、documentroot（ドキュメントのルートディレクトリ）を指定することができます。

## ssl証明書の取得と設定手順
次に、複数のドメインにsslを導入するための手順を説明します。sslを導入することで、ウェブサイトの通信を暗号化し、セキュリティを向上させることができます。

1. ssl証明書の取得
まず、ssl証明書を取得する必要があります。無料で利用できるlet's encryptを使用してssl証明書を取得する方法を説明します。以下のコマンドを使用して、certbotというツールをインストールします。

```bash
sudo apt-get update
sudo apt-get install certbot
```

2. ssl証明書の取得と設定
インストールが完了したら、以下のコマンドを使用してssl証明書を取得します。

```bash
sudo certbot certonly --webroot -w /var/www/html/example -d example.com -d www.example.com
sudo certbot certonly --webroot -w /var/www/html/example2 -d example2.com -d www.example2.com
```

上記の例では、example.comとexample2.comのドメインに対してssl証明書を取得しています。証明書は/var/www/html/exampleと/var/www/html/example2のディレクトリに保存されます。

3. ssl証明書の設定
ssl証明書を取得した後、apacheの設定を変更してsslを有効にします。以下の例では、証明書のパスと証明書のキーのパスを設定しています。

```apache
<virtualhost *:443>
    servername example.com
    documentroot /var/www/html/example

    sslengine on
    sslcertificatefile /etc/letsencrypt/live/example.com/fullchain.pem
    sslcertificatekeyfile /etc/letsencrypt/live/example.com/privkey.pem
</virtualhost>

<virtualhost *:443>
    servername example2.com
    documentroot /var/www/html/example2

    sslengine on
    sslcertificatefile /etc/letsencrypt/live/example2.com/fullchain.pem
    sslcertificatekeyfile /etc/letsencrypt/live/example2.com/privkey.pem
</virtualhost>
```

上記の例では、*:443でlistenを指定し、sslのポートを設定しています。また、sslengineをonにし、sslcertificatefileとsslcertificatekeyfileを正しいパスに設定することでsslを有効化します。

## 複数ドメインのhttpsリダイレクト設定方法
httpsへのリダイレクトを設定することで、ユーザーが常に安全な接続を使用するように促すことができます。

以下の例では、http://example.comをhttps://example.comにリダイレクトする設定方法を説明します。

```apache
<virtualhost *:80>
    servername example.com
    documentroot /var/www/html/example

    rewriteengine on
    rewritecond %{https} off
    rewriterule ^(.*)$ https://%{http_host}%{request_uri} [r=301,l]
</virtualhost>
```

上記の例では、rewritecondを使用してhttpsがオフの場合にリクエストをリダイレクトし、 r=301を使用して永久リダイレクトを行います。

## サブドメインごとの設定とssl対応
サブドメインごとに設定を行い、sslを対応させることもできます。

```apache
<virtualhost *:80>
    servername example.com
    documentroot /var/www/html/example
</virtualhost>

<virtualhost *:80>
    servername subdomain.example.com
    documentroot /var/www/html/subdomain
</virtualhost>
```

上記の例では、example.comとsubdomain.example.comという2つのドメインを設定しています。それぞれのドメインに対して、documentroot（ドキュメントのルートディレクトリ）を指定することができます。

同様にsslに対応させるためには、先ほどのssl証明書の取得と設定手順を行います。

## サイトごとのカスタム設定とドメイン別のリソース管理
複数のドメインを運用する場合、それぞれのサイトにカスタム設定を行いたい場合があります。apacheでは、個別のvirtualhostブロック内でカスタム設定を行うことができます。

以下の例では、example.comとexample2.comそれぞれで異なるカスタム設定を行っています。

```apache
<virtualhost *:80>
    servername example.com
    documentroot /var/www/html/example

    # example.comのカスタム設定
    rewriteengine on
    rewriterule ^page/(.*)$ page.php?id=$1 [l]
</virtualhost>

<virtualhost *:80>
    servername example2.com
    documentroot /var/www/html/example2

    # example2.comのカスタム設定
    rewriteengine on
    rewriterule ^news/(.*)$ news.php?id=$1 [l]
</virtualhost>
```

上記の例では、example.comではurlのリライトを行っています。具体的には、/page/以下のurlをパラメータとしてphpスクリプトに渡しています。

また、example2.comでは、/news/以下のurlをパラメータとしてphpスクリプトに渡しています。

以上が、apacheを使用して複数ドメインのssl対応サイトを構築する方法です。virtualhostを利用することで、1つのサーバーで複数のドメインを運用することができます。let's_encryptを使用してssl証明書を取得し、sslを有効化することで、ウェブサイトのセキュリティを向上させることができます。また、カスタム設定を行うことで、各ドメインごとに異なる機能を実現することも可能です。

参考資料：
- [how to set up multiple ssl certificates on one ip with apache on ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-multiple-ssl-certificates-on-one-ip-with-apache-on-ubuntu-18-04)
- [apache virtual host examples and tutorials](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-centos-7)

　

## 【Apache】関連のまとめ
https://hack-note.com/summary/apache-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

