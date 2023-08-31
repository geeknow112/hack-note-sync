【apache】ディレクトリ別の仮想ホスト設定：複数のブログを管理
apache,virtualhost
apache-virtualhost-directory-based

## ブログ管理のためのディレクトリ別仮想ホスト設定手法

こんにちは。今回は、apacheについて初心者エンジニアに向けて、ディレクトリ別の仮想ホスト設定についてご紹介します。仮想ホスト設定とは、1つの物理的なサーバー上で複数のウェブサイトやブログを運用するための手法です。ディレクトリ別の仮想ホスト設定を行うことで、複数のブログを管理することができます。

ディレクトリ別の仮想ホスト設定手法には、いくつかの方法があります。代表的な2つの手法を以下で紹介します。

### インデックスファイルの設定によるディレクトリ別仮想ホスト
まずは、インデックスファイルの設定によるディレクトリ別の仮想ホスト手法です。この手法では、各ブログのコンテンツを格納するディレクトリを作成し、そのディレクトリに対して仮想ホストを設定します。

例えば、以下のようなディレクトリ構造を考えます。

```
/var/www/html/
├── blog1/
│   ├── index.html
│   └── css/
│       └── style.css
└── blog2/
    ├── index.html
    └── images/
        └── image.jpg
```

この場合、`/var/www/html/blog1`ディレクトリと`/var/www/html/blog2`ディレクトリをそれぞれ別の仮想ホストとして設定することができます。具体的な設定方法は、以下のようになります。

```apacheconf
<virtualhost *:80>
    servername blog1.example.com
    documentroot /var/www/html/blog1
</virtualhost>

<virtualhost *:80>
    servername blog2.example.com
    documentroot /var/www/html/blog2
</virtualhost>
```

これにより、`blog1.example.com`にアクセスすると`/var/www/html/blog1`ディレクトリのコンテンツが表示され、`blog2.example.com`にアクセスすると`/var/www/html/blog2`ディレクトリのコンテンツが表示されるようになります。

### urlパスの設定によるディレクトリ別仮想ホスト
次に、urlパスの設定によるディレクトリ別の仮想ホスト手法です。この手法では、1つのサーバー上に複数のブログのディレクトリを作成せずに、urlパスを使用してブログの切り替えを行います。

例えば、以下のようなurlパスを考えます。

```
http://example.com/blog1
http://example.com/blog2
```

この場合、1つの仮想ホストに対してurlパスごとに異なるコンテンツを表示するように設定します。具体的な設定方法は、以下のようになります。

```apacheconf
<virtualhost *:80>
    servername example.com
    documentroot /var/www/html

    alias /blog1 /var/www/html/blog1
    alias /blog2 /var/www/html/blog2
</virtualhost>
```

これにより、`http://example.com/blog1`にアクセスすると`/var/www/html/blog1`ディレクトリのコンテンツが表示され、`http://example.com/blog2`にアクセスすると`/var/www/html/blog2`ディレクトリのコンテンツが表示されるようになります。

## ブログごとのディレクトリ構造の作成方法

ディレクトリ別の仮想ホスト設定を行う場合、各ブログのコンテンツを格納するためのディレクトリの作成が必要です。以下では、ディレクトリ構造の作成方法について説明します。

まず、ブログごとにディレクトリを作成します。例えば、`/var/www/html`ディレクトリ以下に各ブログのディレクトリを作成します。

```shell
$ mkdir -p /var/www/html/blog1
$ mkdir -p /var/www/html/blog2
```

次に、各ブログのコンテンツ（htmlファイルや画像ファイルなど）を格納するディレクトリを設けます。例えば、`/var/www/html/blog1`ディレクトリにhtmlファイルを設置する場合は、以下のようにします。

```shell
$ touch /var/www/html/blog1/index.html
```

同様に、画像ファイルを設置する場合も同様です。

```shell
$ mkdir /var/www/html/blog1/images
$ cp path/to/image.jpg /var/www/html/blog1/images/
```

このようにして、各ブログのディレクトリ構造を作成することができます。ディレクトリの作成には、`mkdir`コマンドを使用し、ファイルの作成やコピーには`touch`コマンドや`cp`コマンドを使用します。

## ディレクトリ別仮想ホストのアクセス制御とセキュリティ対策

ディレクトリ別の仮想ホスト設定を行う場合、アクセス制御やセキュリティ対策が重要です。以下では、ディレクトリ別の仮想ホストに対するアクセス制御とセキュリティ対策の方法について説明します。

### アクセス制御

ディレクトリ別の仮想ホストに対してアクセス制御を行うためには、apacheの.htaccessファイルを使用する方法があります。具体的な設定方法は以下のようになります。

```apacheconf
<directory "/var/www/html/blog1">
    options followsymlinks
    allowoverride all
    require all granted
</directory>

<directory "/var/www/html/blog2">
    options followsymlinks
    allowoverride all
    require all granted
</directory>
```

これにより、`/var/www/html/blog1`ディレクトリと`/var/www/html/blog2`ディレクトリに対してアクセス制御を設定することができます。上記の設定では、全てのリクエストを許可していますが、必要に応じてipアドレスやユーザー名などによる制限も行うことができます。

### セキュリティ対策

ディレクトリ別の仮想ホストに対するセキュリティ対策として、ssl/tlsの導入やアップデートの実施が重要です。ssl/tlsを使用することで、データの暗号化や通信のセキュリティを確保することができます。

具体的な設定方法は各サーバーによって異なりますが、以下のサイトを参考にして設定を行ってください。

- [let's encrypt](https://letsencrypt.org/)
- [ssl/tls デプロイメント ベストプラクティス](https://info.ssl.com/article.aspx?id=10241)

セキュリティ対策には他にもip制限やファイアウォールの設定、セキュリティパッチの適用などがあります。自社のセキュリティポリシーや要件に基づいて、適切な対策を行ってください。

## ディレクトリ別仮想ホストのログ管理と分析方法

ディレクトリ別の仮想ホストを運用する場合、アクセスログの管理と分析が重要です。以下では、ディレクトリ別仮想ホストのログ管理と分析方法について説明します。

### アクセスログの設定

apacheでは、アクセスログを記録することができます。アクセスログには、アクセスされたurlやリファラなどの情報が記録され、分析に使用することができます。

ログの設定方法は、apacheの設定ファイル（通常は`apache2.conf`や`httpd.conf`）で行います。以下のような設定を追加することで、アクセスログの出力先や書式を指定することができます。

```apacheconf
logformat "%h %l %u %t \"%r\" %>s %b \"%{referer}i\" \"%{user-agent}i\"" combined

customlog /var/log/apache2/access.log combined
```

### ログファイルの分析

アクセスログを分析するためのツールとしては、awstatsやwebalizerなどがあります。これらのツールを使用することで、アクセス解析や統計情報の収集を行うことができます。

例えば、awstatsを使用する場合は、以下のような設定を行います。

```apacheconf
alias /awstatsclasses "/usr/share/awstats/wwwroot/classes/"
alias /awstats-icon "/usr/share/awstats/wwwroot/icon/"
alias /awstatscss "/usr/share/awstats/wwwroot/css/"

scriptalias /awstats/ /usr/lib/cgi-bin/
options execcgi -multiviews +symlinksifownermatch

<location /awstats>
    authtype basic
    authname "restricted access"
    authuserfile /etc/apache2/.awstats.passwd
    require valid-user
</location>
```

上記の設定により、`http://example.com/awstats`にアクセスすることでawstatsの統計情報を閲覧することができます。

## ディレクトリ別仮想ホストのカスタム設定と機能拡張手順

ディレクトリ別の仮想ホストをさらにカスタマイズする場合や、機能を拡張する場合の手順について説明します。

### カスタム設定

ディレクトリ別仮想ホストに対してカスタム設定を行いたい場合は、`.htaccess`ファイルを使用する方法があります。以下のようなコンテンツを含む`.htaccess`ファイルを対象のディレクトリに配置することで、カスタム設定を行うことができます。

```apacheconf
rewriteengine on
rewriterule ^greeting$ greeting.html [l]
```

上記の設定では、`http://example.com/blog1/greeting`にアクセスすると`greeting.html`が表示されるようになります。`.htaccess`ファイルを使用するためには、apacheの設定で`allowoverride`が`all`に設定されている必要があります。

### 機能拡張

ディレクトリ別仮想ホストの機能を拡張する場合、apacheのモジュールやプラグインを使用する方法があります。具体的な拡張方法については、各モジュールやプラグインのドキュメントを参照してください。

以下は、apacheの`mod_rewrite`モジュールを使用したurlリライトの例です。

```apacheconf
rewriteengine on
rewriterule ^blog/([0-9]+)$ blog.php?id=$1 [l]
```

上記の設定では、`http://example.com/blog/123`にアクセスすると`blog.php?id=123`が表示されるようになります。

また、別の拡張方法としては、phpやpythonなどのスクリプト言語を使用することも考えられます。これにより、動的なコンテンツやデータベースとの連携が可能となります。

## まとめ

今回は、apacheを使用してディレクトリ別の仮想ホスト設定を行う方法についてご紹介しました。ディレクトリ別の仮想ホストを利用することで、複数のブログを管理することができます。また、アクセス制御やセキュリティ対策、ログ管理や分析方法、カスタム設定や機能拡張についても説明しました。

これらの手法や設定方法を使用することで、apacheで複数のブログを運営することができます。初心者の方でも、ぜひ挑戦してみてください。

参考文献：
- [apache virtual host documentation](https://httpd.apache.org/docs/current/vhosts/)
- [how to set up apache virtual hosts on ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-18-04)
- [how to set up apache virtual hosts on centos 7](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-centos-7)

　

## 【Apache】関連のまとめ
https://hack-note.com/summary/apache-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

