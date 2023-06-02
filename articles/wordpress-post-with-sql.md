WordPressの記事投稿をSQLでやる方法
WordPress,SQL
wordpress-post-with-sql

# はじめに
WordPressを使って記事を投稿していると、
管理画面の細かい部分で改善したいところが出てくると思います。
ぼくが作業してて改善したいと思った点は下記です。

## 改善したい点
- エディタが使いにくい
- 投稿の要素を一箇所にまとめたい（入力箇所が多い）
- プラグインで解決したくない（プラグインを探すのが面倒）
- テンプレートを強化したい
- 作業を自動化したい

結局、管理画面にログインして、いろいろ設定して、やっとの思いで投稿しているので、
習慣化の妨げになってます。
このあたりをクリアにしてできるだけ投稿作業を簡素化していきます。

# この記事でできるようになること
この記事では、「投稿の要素を一箇所にまとめたい」という要件にフォーカスして、これを改善します。
最終的には、SQLのワンライナーでWordPressへの投稿を目指します。

# WordPressの記事投稿の仕組み
まず、WordPressの投稿の仕組みは下記のようになっています。
1. 管理画面で必要項目を入力して、「公開」ボタンをクリックする。
2. 入力されたテキスト情報を、「wp_posts」テーブルにINSERT。
以上。

つまり、「wp_posts」テーブルにSQL文で直接INSERTすれば、
管理画面をスキップして投稿可能です。

「wp_postmeta」テーブルとか、投稿に関係してそうに思えるテーブルも
シンプルな記事投稿のみなら不要ですが、
SEO関連の情報もワンライナー化したい場合、追加が必要なので、
それは別記事で解説します。

# WordPressの記事投稿用SQL
では、ここからは実際にSQLを考えていきます。

## INSERT先の「wp_posts」テーブル
WordPressのデータベースにアクセスして、wp_postsテーブルの構造を確認します。

```
mysql> desc wp_posts;
+-----------------------+-----------------+------+-----+---------------------+----------------+
| Field                 | Type            | Null | Key | Default             | Extra          |
+-----------------------+-----------------+------+-----+---------------------+----------------+
| ID                    | bigint unsigned | NO   | PRI | NULL                | auto_increment |
| post_author           | bigint unsigned | NO   | MUL | 0                   |                |
| post_date             | datetime        | NO   |     | 0000-00-00 00:00:00 |                |
| post_date_gmt         | datetime        | NO   |     | 0000-00-00 00:00:00 |                |
| post_content          | longtext        | NO   |     | NULL                |                |
| post_title            | text            | NO   |     | NULL                |                |
| post_excerpt          | text            | NO   |     | NULL                |                |
| post_status           | varchar(20)     | NO   |     | publish             |                |
| comment_status        | varchar(20)     | NO   |     | open                |                |
| ping_status           | varchar(20)     | NO   |     | open                |                |
| post_password         | varchar(255)    | NO   |     |                     |                |
| post_name             | varchar(200)    | NO   | MUL |                     |                |
| to_ping               | text            | NO   |     | NULL                |                |
| pinged                | text            | NO   |     | NULL                |                |
| post_modified         | datetime        | NO   |     | 0000-00-00 00:00:00 |                |
| post_modified_gmt     | datetime        | NO   |     | 0000-00-00 00:00:00 |                |
| post_content_filtered | longtext        | NO   |     | NULL                |                |
| post_parent           | bigint unsigned | NO   | MUL | 0                   |                |
| guid                  | varchar(255)    | NO   |     |                     |                |
| menu_order            | int             | NO   |     | 0                   |                |
| post_type             | varchar(20)     | NO   | MUL | post                |                |
| post_mime_type        | varchar(100)    | NO   |     |                     |                |
| comment_count         | bigint          | NO   |     | 0                   |                |
+-----------------------+-----------------+------+-----+---------------------+----------------+
23 rows in set (0.00 sec)
```


主な注意点は下記です。

## ID
auto_incrementなので、NULLをINSERTしたら連番が付与されます。
INSERT文ではNULLに設定しましょう。

## post_content
post_contentフィールドが投稿文章を入れるカラムです。
markdownのエディタプラグインを入れてても、
ここでmarkdown表記がHTMLに変換されるわけではないので、
普通にHTMLで入力しましょう。

そのうちmarkdownをSQLに変換するプログラムを作りたいと思います。

## post_status
記事公開するかどうかの判定値です。「publish」とすることで公開状態でINSERTします。

## post_name
パーマリンクのフィールドです。わかりやすいURLを付けておきましょう。
個人的には管理画面からの投稿でこれが一番面倒な作業でした。
SQL化しておけば先々の一括変更も容易です。

## post_type
投稿か固定ページかの判定値です。投稿の場合「post」、固定ページの場合「page」に設定します。

# サンプルSQL
わかりやすいようにフィールド名をコメントに入れてINSERT文を作成しました。

```
INSERT INTO
# テーブル名
  `wp_posts`
VALUES
  (
# ID (auto_incrementなのでnull)
    null,
# post_author
    1,
# post_date
    current_timestamp,
# post_date_gmt
    (current_timestamp - interval 9 hour),
# post_content
    '<h2>WordPressの記事投稿をSQLでやる方法</h2>\r\n<p>SAMPLE</p>',
# post_title
    'WordPressの記事投稿をSQLでやる方法',
# post_excerpt
    'WordPressの記事投稿をSQLでやる方法',
# post_status
    'publish',
# comment_status
    'close',
# ping_status
    'open',
# post_password
    '',
# post_name
    'wordpress-post-with-sql',
# to_ping
    '',
# pinged
    '',
# post_modified
    current_timestamp,
# post_modified_gmt
    (current_timestamp - interval 9 hour),
# post_content_filtered
    '',
# post_parent
    0,
# guid
    '',
# menu_order
    0,
# post_type
    'post',
# post_mime_type
    '',
# comment_count
    0
  );
```

# WordPressへの自動投稿方法
サンプルSQLをINSERT.sqlとして保存した上で、下記のコマンドを実行します。
```
mysql -u root -p -h localhost wordpress < INSERT.sql
```
rootユーザーでlocalhostのwordpressデータベースにINSERT.sqlを流し込んでいます。
ここではサンプルでファイル名をINSERT.sqlとしていますが、
日付ファイル(例：20220604.sql)や、
パーマリンク名(例：wordpress-post-with-sql.sql)などを用いると
管理しやすくなりおススメです。

## SQLでINSERTした記事画面
正しくHTMLが反映されています。
![](https://storage.googleapis.com/zenn-user-upload/56d13485c10e-20220604.png)

## SQLでINSERTした記事の管理画面
公開設定やパーマリンクが正しく設定されています。
![](https://storage.googleapis.com/zenn-user-upload/3b8f6e54e523-20220604.png)

# まとめ
ワンライナーでの記事投稿方法をまとめると下記です。
1. 記事を作成する。
2. INSERT文に下記4っを埋めてSQLファイルを作る。(他は基本的にサンプルと同じ値でOK)
- post_content
- post_title
- post_excerpt
- post_name
3. mysqlコマンドの実行
```
mysql -u root -p -h localhost wordpress < INSERT.sql
```
4. 画面確認

以上となります。

ここまで読んでいただきましてありがとうございます。
次回は、Docker上にあるWordPressに対してワンライナーで投稿する方法を解説します。

## Wordpress案件を実際に取っていく方法をまとめました
プロのエンジニアになるには、独学を続けるより案件を実際に受注した方が近道です。
フリーランスエンジニアとしてやっていくにはどこかのタイミングで
案件を獲っていかないといけません。
最初から全てうまくいくことは稀でしょう。
となると、うまくいかないことを前提として最速で案件を回していった方が効率的です。

スキルを磨く勉強はほどほどにして、いかにして案件を獲っていくかを考えましょう。

https://hack-note.com/programming/engineer-freelance-wordpress/

