WordPressの記事投稿をSQLでやる方法、に「All in One SEO」要素も追加で。
WordPress,SQL,AiOSEO,SEO
wordpress-post-with-sql-aioseo

# はじめに
https://zenn.dev/gk12/articles/wordpress-post-with-sql
この記事の続きで、SQLによる投稿をするときに、
SEO要素も追加でワンライナーで投稿したいという要件について考察します。

## 改善したい点
- 「All in One SEO」の要素をいちいち埋めるのが面倒

SEO対策で有名なプラグイン「All in One SEO」。
WordPressユーザーならデフォルトで使ってるかと思います。
ただ、やはり登録要素を埋めるのが面倒なので、
SQLによるワンライナーでの効率化を図ります。

# この記事でできるようになること
この記事では、【「All in One SEO」の要素を埋める作業を効率化したい】という要件にフォーカスして、これを改善します。
最終的には、SQLのワンライナーでWordPressへの投稿を目指します。

# 「All in One SEO」の要素登録の仕組み
「All in One SEO」の各要素もWordPressの仕組みに則って、
データベースに保存される仕組みになっています。

つまり、「wp_posts」テーブルに投稿した記事のIDに紐づく
「All in One SEO」の要素フィールドに、SQLで値をUPDATEすることで、
管理画面をスキップして投稿可能です。

前回の記事で保留にした「wp_aioseo_posts」テーブルが、
要素を格納しているテーブルになります。

WordPressでは「All in One SEO」以外でも同じ手法で
「wp_postmeta」に要素フィールドを追加することで、
記事IDに紐づけていろいろ情報を保持していける構造になっています。

# 「All in One SEO」の記事投稿用SQL
では、ここからは実際にSQLを考えていきます。

## UPDATEする「wp_aioseo_posts」テーブル
WordPressのデータベースにアクセスして、wp_aioseo_postsテーブルの構造を確認します。

```
mysql> desc wp_aioseo_posts;
+-----------------------------+-----------------+------+-----+---------+----------------+
| Field                       | Type            | Null | Key | Default | Extra          |
+-----------------------------+-----------------+------+-----+---------+----------------+
| id                          | bigint unsigned | NO   | PRI | NULL    | auto_increment |
| post_id                     | bigint unsigned | NO   | MUL | NULL    |                |
| title                       | text            | YES  |     | NULL    |                |
| description                 | text            | YES  |     | NULL    |                |
| keywords                    | mediumtext      | YES  |     | NULL    |                |
| keyphrases                  | longtext        | YES  |     | NULL    |                |
| page_analysis               | longtext        | YES  |     | NULL    |                |
| canonical_url               | text            | YES  |     | NULL    |                |
| og_title                    | text            | YES  |     | NULL    |                |
| og_description              | text            | YES  |     | NULL    |                |
| og_object_type              | varchar(64)     | YES  |     | default |                |
| og_image_type               | varchar(64)     | YES  |     | default |                |
| og_image_url                | text            | YES  |     | NULL    |                |
| og_image_width              | int             | YES  |     | NULL    |                |
| og_image_height             | int             | YES  |     | NULL    |                |
| og_image_custom_url         | text            | YES  |     | NULL    |                |
| og_image_custom_fields      | text            | YES  |     | NULL    |                |
| og_video                    | varchar(255)    | YES  |     | NULL    |                |
| og_custom_url               | text            | YES  |     | NULL    |                |
| og_article_section          | text            | YES  |     | NULL    |                |
| og_article_tags             | text            | YES  |     | NULL    |                |
| twitter_use_og              | tinyint(1)      | YES  |     | 0       |                |
| twitter_card                | varchar(64)     | YES  |     | default |                |
| twitter_image_type          | varchar(64)     | YES  |     | default |                |
| twitter_image_url           | text            | YES  |     | NULL    |                |
| twitter_image_custom_url    | text            | YES  |     | NULL    |                |
| twitter_image_custom_fields | text            | YES  |     | NULL    |                |
| twitter_title               | text            | YES  |     | NULL    |                |
| twitter_description         | text            | YES  |     | NULL    |                |
| seo_score                   | int             | NO   |     | 0       |                |
| schema_type                 | varchar(20)     | YES  |     | default |                |
| schema_type_options         | longtext        | YES  |     | NULL    |                |
| pillar_content              | tinyint(1)      | YES  |     | NULL    |                |
| robots_default              | tinyint(1)      | NO   |     | 1       |                |
| robots_noindex              | tinyint(1)      | NO   |     | 0       |                |
| robots_noarchive            | tinyint(1)      | NO   |     | 0       |                |
| robots_nosnippet            | tinyint(1)      | NO   |     | 0       |                |
| robots_nofollow             | tinyint(1)      | NO   |     | 0       |                |
| robots_noimageindex         | tinyint(1)      | NO   |     | 0       |                |
| robots_noodp                | tinyint(1)      | NO   |     | 0       |                |
| robots_notranslate          | tinyint(1)      | NO   |     | 0       |                |
| robots_max_snippet          | int             | YES  |     | NULL    |                |
| robots_max_videopreview     | int             | YES  |     | NULL    |                |
| robots_max_imagepreview     | varchar(20)     | YES  |     | large   |                |
| tabs                        | mediumtext      | YES  |     | NULL    |                |
| images                      | longtext        | YES  |     | NULL    |                |
| image_scan_date             | datetime        | YES  |     | NULL    |                |
| priority                    | tinytext        | YES  |     | NULL    |                |
| frequency                   | tinytext        | YES  |     | NULL    |                |
| videos                      | longtext        | YES  |     | NULL    |                |
| video_thumbnail             | text            | YES  |     | NULL    |                |
| video_scan_date             | datetime        | YES  |     | NULL    |                |
| location                    | text            | YES  |     | NULL    |                |
| local_seo                   | longtext        | YES  |     | NULL    |                |
| limit_modified_date         | tinyint(1)      | NO   |     | 0       |                |
| created                     | datetime        | NO   |     | NULL    |                |
| updated                     | datetime        | NO   |     | NULL    |                |
+-----------------------------+-----------------+------+-----+---------+----------------+
57 rows in set (0.00 sec)
```

wp_posts.ID = wp_aioseo_posts.post_idで紐づけて、
wp_aioseo_postsのフィールドにSEO要素を登録していく感じです。

### 注意
wp_postmetaテーブルにもそれらしいフィールドが生成されますが、
こちらは使われてなさそうです。
「_aioseo_***」というそれらしいmeta_keyがあるので、
試しにmeta_value値を変えてみましたが、サイトに反映されず、でした。

```
mysql> select * from wp_postmeta where post_id = '10601';
+---------+---------+---------------------------------------+-----------------------------------------------------+
| meta_id | post_id | meta_key                              | meta_value                                          |
+---------+---------+---------------------------------------+-----------------------------------------------------+
|  104377 |   10601 | _aioseo_title                         | NULL                                                |
|  104378 |   10601 | _aioseo_description                   | NULL                                                |
|  104379 |   10601 | _aioseo_keywords                      |                                                     |
|  104380 |   10601 | _aioseo_og_title                      | NULL                                                |
|  104381 |   10601 | _aioseo_og_description                | NULL                                                |
|  104382 |   10601 | _aioseo_og_article_section            |                                                     |
|  104383 |   10601 | _aioseo_og_article_tags               |                                                     |
|  104384 |   10601 | _aioseo_twitter_title                 | NULL                                                |
|  104385 |   10601 | _aioseo_twitter_description           | NULL                                                |
+---------+---------+---------------------------------------+-----------------------------------------------------+
```

試しにmeta_key = '_aioseo_description'の値を変更。
```
mysql> update wp_postmeta set meta_value = 'sample description' where post_id = '10808' and meta_key = '_aioseo_description';
Query OK, 0 rows affected (0.00 sec)
Rows matched: 1  Changed: 0  Warnings: 0
```

```
mysql> select * from wp_postmeta where post_id = '10808';
+---------+---------+---------------------------------------+-----------------------------------------------------+
| meta_id | post_id | meta_key                              | meta_value                                          |
+---------+---------+---------------------------------------+-----------------------------------------------------+
|  106484 |   10808 | _edit_lock                            | 1654497884:1                                        |
|  106604 |   10808 | _aioseo_title                         | NULL                                                |
|  106605 |   10808 | _edit_last                            | 1                                                   |
|  106620 |   10808 | _aioseo_description                   | sample description                                  |
|  106621 |   10808 | _aioseo_keywords                      |                                                     |
|  106622 |   10808 | _aioseo_og_title                      | NULL                                                |
|  106623 |   10808 | _aioseo_og_description                |                                                     |
|  106624 |   10808 | _aioseo_og_article_section            |                                                     |
|  106625 |   10808 | _aioseo_og_article_tags               |                                                     |
|  106626 |   10808 | _aioseo_twitter_title                 | NULL                                                |
|  106627 |   10808 | _aioseo_twitter_description           | NULL                                                |
+---------+---------+---------------------------------------+-----------------------------------------------------+

```
フィールドの値は変わっているけど、HTMLには反映されていません。
また、meta_valueをSQLで修正していても、管理画面から再度記事を更新すると、NULLに置き換わります。


## 「wp_aioseo_posts」のフィールドへのUPDATE文
本題に戻って、ここではSEOでメインとなる下記の2つをSQLでINSERTしてみます。
- wp_aioseo_posts.title
- wp_aioseo_posts.description

```
mysql> update wp_aioseo_posts set title = 'sample TITLE', description = 'sample description' where post_id = '10808';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

```

```
mysql> select title, description from wp_aioseo_posts where post_id = '10808' \G;
*************************** 1. row ***************************
      title: sample TITLE
description: sample description
1 row in set (0.00 sec)

```

## SQLでUPDATEした記事画面
正しくHTMLが反映されています。
![](https://storage.googleapis.com/zenn-user-upload/5c2f74372bcc-20220606.png)

## SQLでUPDATEした記事の管理画面
Wordpress管理画面のAIOSEO設定で下記の項目にUPDATEした値が反映されています。
- Snippet Preview
- 投稿 Title
- Meta Description
![](https://storage.googleapis.com/zenn-user-upload/809eb1c07b11-20220606.png)

# まとめ
AIOSEOのフィールドをSQLで更新する方法をまとめると下記です。
1. wp_aioseo_postsテーブルの更新したい要素をUPDATE文に追加する。
2. mysql上でコマンド実行、または、msqlコマンドで実行
```
mysql -u root -p -h localhost wordpress < UPDATE.sql
```
4. 画面確認

以上となります。

ここまで読んでいただきましてありがとうございます。
次回は、これらのSQLを使って一括インポートする処理を解説します。

## Wordpress案件を実際に取っていく方法をまとめました
プロのエンジニアになるには、独学を続けるより案件を実際に受注した方が近道です。
フリーランスエンジニアとしてやっていくにはどこかのタイミングで
案件を獲っていかないといけません。
最初から全てうまくいくことは稀でしょう。
となると、うまくいかないことを前提として最速で案件を回していった方が効率的です。

スキルを磨く勉強はほどほどにして、いかにして案件を獲っていくかを考えましょう。

https://hack-note.com/programming/engineer-freelance-wordpress/

