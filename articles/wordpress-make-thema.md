【初心者向け】wordpressのテーマを爆速で作る方法
wordpress,thema,作り方
wordpress-make-thema

こんにちは。今回は、wordpressについて初心者エンジニアに向けて、テーマの作り方について解説します。

wordpressは、オープンソースのcms(content management system)です。誰でも無料で利用できるため、多くの人々に愛され、世界的にも広く使われています。wordpressを利用することで、ユーザーは簡単にウェブサイトを作成できます。

しかし、wordpress本体には自分自身のブランドイメージにあったカスタマイズやレイアウトの変更ができません。そこで、wordpressテーマが登場します。テーマをインストールすることで、wordpressサイトのデザインを自分の好みに合わせることができます。

以下では、wordpressテーマの作り方について解説します。

## テーマの作成方法

まずは、テーマを作成するために必要なものを用意しましょう。

1. テキストエディター（visual studio code、sublime text、atomなど）
2. ftpクライアント（filezillaなど）
3. コーディングスキル
4. wordpressの基本的な知識

テーマを作成するために必要な最低限のフォルダーとファイルは以下の通りです。

```
your_theme
|__ index.php
|__ style.css
|__ functions.php
|__ screenshot.png
|__ js/
|__ css/
|__ img/
|__ inc/
```

- index.php: wordpressテーマのメインファイルです
- style.css: wordpressテーマのスタイルを定義するファイルです
- functions.php: wordpressテーマに機能を追加するためのファイルです
- screenshot.png: wordpressのダッシュボードで、テーマのスクリーンショットとして表示される画像です

その他のフォルダーは、wordpressテーマによって必要に応じて追加されます。例えば、以下のようなものがあります。

- js/: 関数ファイルやプラグインのスクリプトファイルを保存するフォルダー
- css/: スタイルシートファイルを保存するフォルダー
- img/: 画像ファイルを保存するフォルダー
- inc/: 処理や機能をまとめたファイルを保存するフォルダー

作成したテーマは、wordpressの/wp-content/themes/ディレクトリーに保存します。テーマフォルダーの名前は、フォルダー内のスタイルシートのテンプレートタグのテーマ名と一致している必要があります。

## wordpressテーマの構成

wordpressテーマには、大きく分けて3つのパーツがあります。

1. header
2. content
3. footer

headerには、タイトルやメニュー、ロゴ、サイトの説明などが表示されます。contentには、記事の本文や画像、動画、テキストが表示されます。footerには、著作権表示や挨拶文、snsのアイコンなどが表示されます。

それぞれのパーツは、少なくとも1つのphpファイルによって構成され、それらをindex.phpに組み込んでいます。例えば、header.php、content.php、footer.phpなどに分けて作成することが一般的です。

以下は、wordpressテーマの基本的な構成の例です。

```
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo( 'charset' ); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title><?php the_title(); ?></title>
  <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
  <?php get_header(); ?>
  <div id="content">
    <div id="main">
      <?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
        <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
        <?php the_content(); ?>
      <?php endwhile; endif; ?>
    </div><!-- end #main -->
    <?php get_sidebar(); ?>
  </div><!-- end #content -->
  <?php get_footer(); ?>
  <?php wp_footer(); ?>
</body>
</html>
```

wordpressテーマは、このように構成されています。

## wordpressテーマの作成手順

以下は、wordpressテーマを作成する手順です。

1. 適当なフォルダを作成する（例：my-theme）
2. my-themeフォルダに必要なファイルを作成する
3. my-themeフォルダをwordpressの/wp-content/themes/ディレクトリーにアップロードする
4. wordpressのダッシュボードで、作成したテーマを有効にする
5. テーマのデザインを調整する（html、css、javascript、画像の追加など）

## まとめ

wordpressテーマの作成方法について解説しました。wordpressテーマは、自分自身のブランドイメージにあったデザインにすることができるため、ウェブサイトの魅力を高めることができます。

wordpressテーマの作成には、コーディングスキルが必要になります。しかし、wordpressテーマの作り方について理解することで、自分自身でカスタマイズすることができます。

最後に、wordpressテーマの作成に役立つサンプルコードを2つご紹介します。

1. レスポンシブ対応のwordpressテーマの作成方法
```css
@media (max-width: 768px) {
    /* スマートフォン用のcss */
}
@media (min-width: 769px) {
    /* pc用のcss */
}
```

2. wordpressのカスタム投稿タイプの作成方法
```php
function custom_post_type() {
    $labels = array(
        'name' => 'クーポン',
        'singular_name' => 'クーポン',
        'add_new' => '新規追加',
        'add_new_item' => '新規クーポンを追加',
        'edit_item' => 'クーポンを編集',
        'new_item' => '新しいクーポン',
        'view_item' => 'クーポンを表示',
        'search_items' => 'クーポンを検索',
        'not_found' => 'クーポンはありません',
        'not_found_in_trash' => 'ゴミ箱にクーポンはありません'
    );

    $args = array(
        'labels' => $labels,
        'public' => true,
        'menu_position' => 5,
        'menu_icon' => 'dashicons-tickets-alt',
        'supports' => array(
            'title',
            'editor',
            'thumbnail',
            'custom-fields'
        ),
        'has_archive' => true,
        'rewrite' => array('slug' => 'coupon'),
    );

    register_post_type('coupon', $args);
}

add_action('init', 'custom_post_type');
```

wordpressテーマの作成には、熱意と忍耐が必要です。しかし、wordpressにはカスタマイズがしやすいという特徴があるため、自分自身でカスタマイズしてみることをおすすめします。

## 参考文献

1. [how to create a wordpress theme from scratch: part 1](https://www.taniarascia.com/developing-a-wordpress-theme-from-scratch/)
2. [how to create a wordpress theme from scratch: part 2](https://www.taniarascia.com/developing-a-wordpress-theme-from-scratch-continued/)

## Wordpress案件を実際に取っていく方法をまとめました
プロのエンジニアになるには、独学を続けるより案件を実際に受注した方が近道です。
フリーランスエンジニアとしてやっていくにはどこかのタイミングで
案件を獲っていかないといけません。
最初から全てうまくいくことは稀でしょう。
となると、うまくいかないことを前提として最速で案件を回していった方が効率的です。

スキルを磨く勉強はほどほどにして、いかにして案件を獲っていくかを考えましょう。

https://hack-note.com/programming/engineer-freelance-wordpress/

