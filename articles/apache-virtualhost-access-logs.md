【apache】ログファイルの管理と解析：virtualhostでアクセスログを取得する手順
apache,virtualhost
apache-virtualhost-access-logs

## apacheについて初心者エンジニアに向けて、ログファイルの管理と解析：virtualhostでアクセスログを取得する手順

こんにちは。今回は、apacheについて初心者エンジニアに向けて、ログファイルの管理と解析の方法についてご紹介します。特に、virtualhostを使用してアクセスログを取得する手順に焦点を当てて解説していきます。

### アクセスログの有効化とフォーマット設定方法

まず最初に、apacheでのアクセスログの有効化とフォーマット設定方法について説明します。

apacheの設定ファイルである`httpd.conf`を編集します。まず、アクセスログが有効になっていることを確認します。以下のような行が存在するかどうかを確認しましょう。

```apache
customlog logs/access_log common
```

存在しない場合は、`#`を取り除いてコメントアウトを解除し、`common`の部分はアクセスログのフォーマットに対応する文字列に置き換えます。例えば、以下のようなフォーマットを指定することもできます。

```apache
customlog logs/access_log "%h %l %u %t \"%r\" %>s %b"
```

フィールドの詳細については、apacheの公式ドキュメントを参照してください。

参考記事：
- [apache logging basics](https://httpd.apache.org/docs/2.4/logs.html)

### アクセスログの保存場所とファイル名のカスタマイズ手順

次に、アクセスログの保存場所とファイル名のカスタマイズ手順について説明します。

apacheの設定ファイルである`httpd.conf`を再度編集します。以下のように、アクセスログの保存場所をカスタマイズすることができます。

```apache
customlog /var/log/httpd/access.log common
```

上記の例では、`/var/log/httpd/`というディレクトリに`access.log`というファイル名でアクセスログが保存されます。必要に応じてファイル名や保存場所を変更してください。

### ログのローテーションと古いログの削除方法

アクセスログを長期間保存すると、ディスク容量の問題が発生する可能性があります。そのため、ログのローテーションと古いログの削除方法を知っておくことが重要です。

apacheでは、ログのローテーションと削除を自動化するために、`logrotate`というツールを利用することができます。まず、`logrotate`の設定ファイルを作成します。

```bash
sudo nano /etc/logrotate.d/httpd
```

以下のような内容を記述します。

```
/var/log/httpd/access.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    create 644 root root
    sharedscripts
    postrotate
        /sbin/service httpd reload > /dev/null 2>/dev/null || true
    endscript
}
```

上記の例では、ログを毎日ローテーションし、古いログファイルを7つまで保持します。また、ログを圧縮してディスク容量を節約します。

### アクセスログの解析ツールと重要な情報の抽出方法

アクセスログには、ウェブサーバーにアクセスしたクライアントのipアドレスやリクエストのurlなど、重要な情報が含まれています。このような情報を抽出するための解析ツールを使うことで、ウェブサーバーのトラフィックや利用者の行動を把握することができます。

代表的なアクセスログ解析ツールとしては、以下のものがあります。

- awstats
- webalizer
- goaccess

これらのツールは、ログファイルを解析し、解析結果を可視化して表示することができます。

参考記事：
- [analyze apache logs with awstats](https://www.digitalocean.com/community/tutorials/how-to-analyze-apache-logs-on-ubuntu-16-04)
- [how to use webalizer to analyze apache web logs on ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-use-webalizer-to-analyze-apache-web-logs-on-ubuntu-14-04)
- [how to analyze apache logs with goaccess on ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-analyze-apache-logs-with-goaccess-on-ubuntu-18-04)

### リモートipアドレスのブロックとセキュリティ対策のためのログ分析

最後に、アクセスログの解析を活用してリモートipアドレスのブロックやセキュリティ対策のためのログ分析について説明します。

アクセスログには、不正なアクセスやボットによるスキャンなど、セキュリティ上の脅威が写し出されることがあります。これらの脅威を特定し、リモートipアドレスをブロックすることで、サイトのセキュリティを向上させることができます。

例えば、以下のようなコマンドを使用して、アクセスログから特定の条件を満たすリモートipアドレスを抽出することができます。

```bash
grep "404" /var/log/httpd/access.log | awk '{print $1}'
```

上記の例では、`404`という文字列を含む行を抽出し、その中のリモートipアドレスを表示します。

これらの抽出結果をもとに、適切な対策を講じることができます。

以上が、apacheのログファイルの管理と解析についての基本的な手順です。初心者の方でも、これらの手順を実践することで、apacheのログファイルを効果的に管理し、セキュリティ対策に役立てることができるでしょう。進んでいくと、より高度なログ解析やセキュリティ対策の手法にも取り組むことができますので、ぜひ挑戦してみてください。

　

## 【Apache】関連のまとめ
https://hack-note.com/summary/apache-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

