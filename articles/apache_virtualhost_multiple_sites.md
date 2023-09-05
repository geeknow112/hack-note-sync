【apache】複数のサイトをホストするためのvirtualhostの設定方法
apache,virtualhost,aws,lightsail,let's_encrypt,ssl
apache_virtualhost_multiple_sites

こんにちは。今回は、apacheについて初心者エンジニアに向けて、複数のサイトをホストするためのvirtualhostの設定方法についてご説明します。

## virtualhostの基本概念と設定手順
apacheのvirtualhostは、1つのサーバ上で複数のドメインやサイトをホストするための機能です。1つのipアドレスに複数のドメインを紐付けることで、異なるドメインに対して異なるコンテンツや設定を提供することが可能となります。

では、具体的な設定手順を見ていきましょう。

まずは、apacheの設定ファイルを編集します。設定ファイルは通常、`/etc/apache2/sites-available/`ディレクトリに格納されています。以下のコマンドで設定ファイルを作成します。

```
sudo nano /etc/apache2/sites-available/example.com.conf
```

`example.com`の部分は、ホストするドメインに合わせて適宜変更してください。

次に、以下のような設定を追記します。

```apacheconf
<virtualhost *:80>
    servername example.com
    documentroot /var/www/html/example.com
    <directory /var/www/html/example.com>
        options indexes followsymlinks
        allowoverride all
        require all granted
    </directory>
    errorlog ${apache_log_dir}/example.com_error.log
    customlog ${apache_log_dir}/example.com_access.log combined
</virtualhost>
```

上記の設定ではポート80（http）でリクエストを受け付け、`example.com`というドメインに対して`/var/www/html/example.com`ディレクトリをドキュメントルートとして指定しています。また、エラーログとアクセスログも設定しています。

設定を保存したら、設定ファイルを有効化します。

```
sudo a2ensite example.com.conf
```

最後に、apacheを再起動して設定を反映させます。

```
sudo service apache2 restart
```

これで、`example.com`というドメインに対してapacheが正しく設定され、コンテンツを提供する準備が整いました。

## 複数のサイトを識別するためのservernameとserveraliasの活用方法
apacheでは、`servername`ディレクティブを使用して特定のドメインを識別することができます。また、複数のドメインやサブドメインへのアクセスを許可する場合には、`serveralias`ディレクティブを使用することもできます。

たとえば、以下のような設定を考えてみましょう。

```apacheconf
<virtualhost *:80>
    servername example.com
    serveralias www.example.com blog.example.com
    documentroot /var/www/html/example.com
    ...
</virtualhost>
```

上記の設定では、`example.com`だけでなく、`www.example.com`と`blog.example.com`も同じドキュメントルートでアクセスできるようになります。

## 各サイトのルートディレクトリの設定とドキュメントルートの指定方法
apacheでは、サイトごとに異なるルートディレクトリを指定することができます。ルートディレクトリは、サイトのコンテンツが格納されるベースとなるディレクトリです。

ルートディレクトリの指定は、先ほどの設定例でも見たように`documentroot`ディレクティブを使用して行います。例えば、以下のような設定です。

```apacheconf
<virtualhost *:80>
    servername example.com
    documentroot /var/www/html/example.com
    ...
</virtualhost>

<virtualhost *:80>
    servername blog.example.com
    documentroot /var/www/html/blog.example.com
    ...
</virtualhost>
```

上記の例では、`example.com`と`blog.example.com`それぞれに対して異なるルートディレクトリを指定しています。このようにすることで、複数のサイトを独立してホストすることができます。

## サイトごとのログの分離とカスタムログフォーマットの設定手法
apacheでは、サイトごとにログファイルを分割して管理することができます。これにより、各サイトのアクセスログとエラーログを独立して管理することができます。

ログの分離は、先ほどの設定例でも見たように`errorlog`と`customlog`ディレクティブを使用して行います。以下は具体的な例です。

```apacheconf
<virtualhost *:80>
    servername example.com
    documentroot /var/www/html/example.com
    errorlog ${apache_log_dir}/example.com_error.log
    customlog ${apache_log_dir}/example.com_access.log combined
    ...
</virtualhost>

<virtualhost *:80>
    servername blog.example.com
    documentroot /var/www/html/blog.example.com
    errorlog ${apache_log_dir}/blog.example.com_error.log
    customlog ${apache_log_dir}/blog.example.com_access.log combined
    ...
</virtualhost>
```

上記の例では、`example.com`と`blog.example.com`それぞれに対して異なるエラーログとアクセスログを設定しています。ログファイル名は、`${apache_log_dir}`を使用することでapacheのデフォルトのログディレクトリに書き込むようになります。

また、`customlog`ディレクティブでは、ログフォーマットをカスタマイズすることもできます。デフォルトでは`combined`というフォーマットが使用されますが、必要に応じて変更することができます。

## バーチャルホストの優先順位とデフォルトホストの設定方法
apacheでは、複数のバーチャルホストが設定されている場合、どのホストをデフォルトとするかや、優先順位についても設定することができます。

デフォルトホストは、どのドメインにもマッチしないリクエストが来た場合に使用されるホストです。デフォルトホストは、`000-default.conf`という名前の設定ファイルで設定します。

まずは、デフォルトホストを設定しましょう。以下のコマンドで`000-default.conf`ファイルを編集します。

```
sudo nano /etc/apache2/sites-available/000-default.conf
```

次に、以下のような設定を追記します。

```apacheconf
<virtualhost *:80>
    servername default
    documentroot /var/www/html/default
    ...
</virtualhost>
```

上記の設定では、どのドメインにもマッチしないリクエストが来た場合に、`default`というドキュメントルートを使用するようになります。この部分は、適宜変更してください。

優先順位については、apacheは設定ファイルの読み込み順に処理されます。そのため、より具体的なドメイン名のバーチャルホストが優先されます。例えば、以下のような設定がある場合、`example.com`のバーチャルホストが優先されます。

```apacheconf
<virtualhost *:80>
    servername example.com
    documentroot /var/www/html/example.com
    ...
</virtualhost>

<virtualhost *:80>
    servername blog.example.com
    documentroot /var/www/html/blog.example.com
    ...
</virtualhost>
```

設定ファイルの読み込み順に気をつけながら、優先順位を意識して設定を行ってください。

以上が、apacheで複数のサイトをホストするためのvirtualhostの設定方法についてのご説明でした。apacheの仕組みや設定ファイルの編集方法について理解が深まったことと思います。

参考記事:
- [how to set up apache virtual hosts on ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-18-04)
- [apache virtual host examples](https://httpd.apache.org/docs/2.4/vhosts/examples.html)

　

## 【Apache】関連のまとめ
https://hack-note.com/summary/apache-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

