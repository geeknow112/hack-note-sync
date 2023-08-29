<!--
title: 【apache】virtualhost設定：複数ドメインのブログをホストしよう
tags: apache,virtualhost
id: 
private: false
-->

## 複数ドメインの仮想ホストの設定手順

複数のドメインを同じサーバで運用するためには、apacheの仮想ホスト（virtualhost）を設定する必要があります。以下に、複数ドメインの仮想ホストの設定手順を説明します。

まず、apacheの設定ファイル（httpd.confまたはapache2.conf）を編集します。このファイルは、通常は/etc/httpd/conf/httpd.confや/etc/apache2/apache2.confにあります。

1. apacheの設定ファイルを開きます。
```
$ sudo vim /etc/httpd/conf/httpd.conf
```
または
```
$ sudo vim /etc/apache2/apache2.conf
```

2. 仮想ホストの設定を追加します。以下は例です。
```
<virtualhost *:80>
    servername www.example1.com
    documentroot /var/www/example1
</virtualhost>

<virtualhost *:80>
    servername www.example2.com
    documentroot /var/www/example2
</virtualhost>
```

3. 上記の例では、www.example1.comとwww.example2.comという2つのドメインに対して、それぞれのドキュメントルートを設定しています。適宜、servername（ドメイン名）とdocumentroot（ドキュメントルート）を変更してください。

4. 設定ファイルを保存し、apacheを再起動します。
```
$ sudo systemctl restart httpd
```
または
```
$ sudo systemctl restart apache2
```

これで、複数のドメインを同じサーバで運用するための仮想ホストの設定が完了しました。

参考ブログ記事：
- [apache virtual host](https://www.linode.com/docs/guides/how-to-set-up-apache-virtual-hosts-on-ubuntu-18-04/)
- [how to set up apache virtual hosts on centos 7](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-centos-7)

## ドメイン別のディレクトリ構造の作成方法

複数のドメインを運営する場合、それぞれのドメインごとに異なるコンテンツを提供する必要があります。そのためには、ドメイン別にディレクトリ構造を作成する必要があります。以下に、ドメイン別のディレクトリ構造の作成方法を説明します。

1. ドキュメントルートのディレクトリに移動します。
```
$ cd /var/www
```

2. ドメインごとにディレクトリを作成します。以下は例です。
```
$ sudo mkdir example1
$ sudo mkdir example2
```

3. 各ドメインのディレクトリに、それぞれのコンテンツを配置します。
```
$ sudo cp /path/to/example1/index.html /var/www/example1
$ sudo cp /path/to/example2/index.html /var/www/example2
```

4. アクセス権を設定します。
```
$ sudo chown -r apache:apache /var/www/example1
$ sudo chown -r apache:apache /var/www/example2
```

以上で、ドメイン別のディレクトリ構造の作成が完了しました。

参考ブログ記事：
- [apache virtual host](https://www.linode.com/docs/guides/how-to-set-up-apache-virtual-hosts-on-ubuntu-18-04/)
- [how to set up apache virtual hosts on centos 7](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-centos-7)

## サブドメインの仮想ホストの設定手順

サブドメインとは、通常のドメインに続くドメイン名の一部であり、異なるコンテンツを提供するために使用されます。apacheでは、サブドメインの仮想ホストを設定することができます。以下に、サブドメインの仮想ホストの設定手順を説明します。

1. apacheの設定ファイルを開きます。
```
$ sudo vim /etc/httpd/conf/httpd.conf
```
または
```
$ sudo vim /etc/apache2/apache2.conf
```

2. 仮想ホストの設定を追加します。以下は例です。
```
<virtualhost *:80>
    servername example1.com
    documentroot /var/www/example1
</virtualhost>

<virtualhost *:80>
    servername sub.example1.com
    documentroot /var/www/sub
</virtualhost>
```

3. 上記の例では、example1.comというドメインとそのサブドメインであるsub.example1.comに対して、それぞれのドキュメントルートを設定しています。適宜、servername（ドメイン名）とdocumentroot（ドキュメントルート）を変更してください。

4. 設定ファイルを保存し、apacheを再起動します。
```
$ sudo systemctl restart httpd
```
または
```
$ sudo systemctl restart apache2
```

これで、サブドメインの仮想ホストの設定が完了しました。

参考ブログ記事：
- [how to create apache virtual host for subdomains](https://www.tecmint.com/apache-server-virtual-host-configuration-for-subdomain/)
- [apache virtual host](https://www.linode.com/docs/guides/how-to-set-up-apache-virtual-hosts-on-ubuntu-18-04/)

## ssl証明書の適用とhttps接続の設定方法

ssl証明書を適用し、https接続を設定することによって、通信の暗号化やセキュリティの向上を図ることができます。以下に、ssl証明書の適用とhttps接続の設定方法を説明します。

1. ssl証明書を取得します。以下は、let's encryptを使用してssl証明書を取得する場合の例です。
```
$ sudo certbot --apache -d example.com -d www.example.com
```

2. ssl証明書の適用とhttps接続の設定が完了しました。

参考ブログ記事：
- [how to secure apache with let's encrypt certificates on centos 7](https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-centos-7)
- [how to set up apache with a free signed ssl/tls certificate on centos 8](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-with-a-free-signed-ssl-tls-certificate-on-a-vps)

## 仮想ホストのテストとトラブルシューティングのポイント

仮想ホストの設定が正しく行われているかをテストし、必要な場合にはトラブルシューティングを行うことが重要です。以下に、仮想ホストのテストとトラブルシューティングのポイントを説明します。

1. 仮想ホストの設定が正しいかをテストするために、ブラウザで各ドメインにアクセスしてみます。

2. アクセスが正常に行われない場合、以下の点を確認してください。
   - 設定ファイルにエラーがないかを確認します。
   - 設定ファイルの変更後にapacheを再起動しているかを確認します。
   - ドキュメントルートのパーミッションが正しく設定されているかを確認します。
   - サーバのファイアウォールやセキュリティグループの設定が正しいかを確認します。
   - dnsの設定が正しいかを確認します。

以上のポイントを確認し、必要な場合は修正を行ってください。

参考ブログ記事：
- [apache virtual host](https://www.linode.com/docs/guides/how-to-set-up-apache-virtual-hosts-on-ubuntu-18-04/)
- [troubleshooting apache virtual hosts](https://brianpartridge.com/article/apache-virtualhost-troubleshooting)

　

## 【Apache】関連のまとめ
https://hack-note.com/summary/apache-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)
