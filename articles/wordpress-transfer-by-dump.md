【基礎】Wordpressの記事データだけ、dumpファイルで移行するには
Wordpress,mysql,dump
wordpress-transfer-by-dump

こんにちは。今回は、Wordpressについて初心者エンジニアに向けて、Wordpressの記事データだけをdumpファイルで移行する方法について解説していきます。

## WordpressのDBテーブル定義

WordpressのDBには、以下のようなテーブルが存在します。

| テーブル名 | 内容 |
| --- | --- |
| wp_posts | 記事の本文やタイトル、投稿者などの情報を格納する。 |
| wp_postmeta | 記事のメタ情報（例：タグ、カテゴリー、投稿日時など）を格納する。 |
| wp_terms | 記事のタグやカテゴリーの情報を格納する。 |
| wp_term_relationships | 記事とタグ、カテゴリーの関係性を格納する。 |
| wp_term_taxonomy | タグやカテゴリーの分類情報を格納する。 |

それぞれのテーブルの役割は、以下の通りです。

- wp_posts: 記事の本文やタイトル、投稿者などの情報を格納する。
- wp_postmeta: 記事のメタ情報（例：タグ、カテゴリー、投稿日時など）を格納する。
- wp_terms: 記事のタグやカテゴリーの情報を格納する。
- wp_term_relationships: 記事とタグ、カテゴリーの関係性を格納する。
- wp_term_taxonomy: タグやカテゴリーの分類情報を格納する。

## Wordpressの記事データの格納先

Wordpressの記事データは、テーブルwp_postsに格納されています。各記事には、以下のような情報が格納されています。

| カラム名 | 内容 |
| --- | --- |
| ID | 記事のID |
| post_author | 記事の投稿者 |
| post_date | 記事の投稿日時 |
| post_content | 記事の本文 |
| post_title | 記事のタイトル |
| post_excerpt | 記事の抜粋 |
| post_status | 記事のステータス（公開、下書き、削除など） |
| comment_status | コメントのステータス（許可、禁止など） |
| ping_status | トラックバックのステータス（許可、禁止など） |
| post_password | 記事のパスワード（設定されている場合） |
| post_name | 記事のURLスラッグ |
| to_ping | トラックバックの送信先URL |
| pinged | トラックバックが送信されたURL |
| post_modified | 記事の更新日時 |
| post_content_filtered | フィルタされた記事本文 |

## Wordpressの記事データだけdumpで移行するには

Wordpressの記事データだけをdumpファイルで移行するには、以下の手順を実行します。

1. MySQLのデータベースにログインする。

```
mysql -u ユーザ名 -p パスワード データベース名
```

2. データベース内のwp_postsテーブルをdumpする。

```
mysqldump -u ユーザ名 -p パスワード データベース名 wp_posts > dumpファイル名.sql
```

3. dumpファイルを転送する。

ダンプファイルを転送する方法は、様々ありますが、FTPを使う場合は、以下の手順を実行します。

- FTPクライアントを起動して、WordPressのインストール先に接続する。
- ダンプファイルをサーバーにアップロードする。

4. データベースにインポートする。

```
mysql -u ユーザ名 -p パスワード データベース名 < dumpファイル名.sql
```

これで、wp_postsテーブルの記事データがインポートされます。

## 注意点

- ダンプファイルを作成する前に、必ずバックアップを取っておくこと。
- wp_postsテーブルには、記事以外の情報も含まれているため、全てのテーブルをインポートする必要がある場合がある。
- ダンプファイルのサイズが大きい場合は、ファイル転送に時間がかかるため、注意が必要。
- インポートする前に、データベースの文字コード、照合順序が同じであることを確認すること。
- インポート後に、WordPressの設定で、パーマリンクの再設定を行う必要がある場合がある。

以上が、Wordpressの記事データだけをdumpファイルで移行する方法についての解説でした。もし、他にも参考になる情報があれば、以下のブログ記事を参考にしてください。

- [WordPress の記事データだけをエクスポート・インポートする方法](https://www.webdesignleaves.com/wp/wordpress/614/)
- [WordPressの投稿データをダンプしてバックアップする方法](https://www.softel.co.jp/blogs/tech/archives/675) 

>注意点を守らない場合、データの消失や破損などが起きる可能性があるため、非常に注意が必要です。

以上で、Wordpressの記事データだけをdumpファイルで移行する方法についての解説を終えます。

## Wordpressを学ぶには下記もおススメ
- [TechAcademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3A%2F%2Ftechacademy.jp%2Fhtmlcss-trial%3Futm_source%3Dmoshimo%26utm_medium%3Daffiliate%26utm_campaign%3Dtextad)
- [オンラインスクール DMM WEBCAMP PRO](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=ON)


## Wordpress案件を実際に取っていく方法をまとめました
プロのエンジニアになるには、独学を続けるより案件を実際に受注した方が近道です。
フリーランスエンジニアとしてやっていくにはどこかのタイミングで
案件を獲っていかないといけません。
最初から全てうまくいくことは稀でしょう。
となると、うまくいかないことを前提として最速で案件を回していった方が効率的です。

スキルを磨く勉強はほどほどにして、いかにして案件を獲っていくかを考えましょう。

https://hack-note.com/programming/engineer-freelance-wordpress/

