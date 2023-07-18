【django】静的ファイルの扱い方：cssやjavascriptを読み込む方法
python,django
django-static-contents

## 静的ファイルの役割と必要性とは？

静的ファイルとは、ユーザーがwebサイトを閲覧する際に必要なcssファイルやjavascriptファイルなどのリソースを指します。これらの静的ファイルはサーバーに保存され、クライアントのブラウザから必要に応じてリクエストされます。静的ファイルは、ウェブページのレイアウトやデザイン、インタラクティブな要素の作成に不可欠な役割を果たしており、ウェブ開発において欠かせないものです。

静的ファイルの必要性は、ウェブ開発においてパフォーマンスの向上やメンテナンスの容易化に関係しています。cssやjavascriptなどのスタイルシートやスクリプトファイルを個別のファイルとして管理することで、コードの再利用性や保守性が高まります。また、ブラウザはこれらの静的ファイルをキャッシュし、再利用することでウェブページの読み込み速度を向上させることもできます。

静的ファイルの扱い方については、フレームワークやツールによって異なりますが、djangoでは特定のディレクトリに静的ファイルを配置し、専用のタグを使用してhtmlテンプレートに読み込む方法が一般的です。次のセクションでは、djangoでの静的ファイルの扱い方について詳しく解説します。

参考ブログ記事：
- [django公式ドキュメント - managing static files　(英語)](https://docs.djangoproject.com/en/3.2/howto/static-files/)
- [djangoアプリケーション開発で使う静的ファイルの配置方法](https://qiita.com/felyce/items/2ddb3da9a1f61be0ebc5)

## djangoで静的ファイルを扱う方法とは？

djangoでは、静的ファイルを扱うための仕組みが用意されています。まず、`settings.py`ファイルの中にある`static_url`と`static_root`という2つの設定が必要です。`static_url`は、静的ファイルへのurlを定義するものであり、通常は`/static/`と設定します。`static_root`は、静的ファイルが集約されるディレクトリのパスを指定します。

次に、アプリケーションごとに静的ファイルを配置するディレクトリを決める必要があります。通常は各アプリケーションのルートディレクトリに`static`というディレクトリを作成し、その中に静的ファイルを配置します。このディレクトリ構造は自由に決められますが、一般的にはdjangoが推奨する構成に従った方が良いでしょう。

静的ファイルの配置が完了したら、htmlテンプレートに静的ファイルを読み込むためのタグを追加します。djangoでは、`{% load static %}`というタグを使用して静的ファイルの読み込みを指定します。具体的な読み込み方法は後述します。

参考ブログ記事：
- [django公式ドキュメント - managing static files　(英語)](https://docs.djangoproject.com/en/3.2/howto/static-files/)
- [djangoの静的ファイルの扱い方](https://blog.hirokiky.org/entry/2019/09/16/214031)

## 静的ファイルの配置場所とディレクトリ構成の決め方

静的ファイルの配置場所とディレクトリ構成は、djangoのプロジェクト構造や開発チームのルールによって異なる場合があります。しかし、一般的なベストプラクティスとして、djangoが推奨する構成に従った方が良いでしょう。

まず、djangoのプロジェクトのルートディレクトリには、`static`というディレクトリを作成します。このディレクトリには、プロジェクト全体で使用する静的ファイルを配置します。例えば、共通のcssファイルやjavascriptファイルなどが該当します。

次に、各アプリケーションのルートディレクトリにも`static`というディレクトリを作成します。このディレクトリには、各アプリケーションごとに必要な静的ファイルを配置します。例えば、特定のアプリケーションで使用するcssファイルやjavascriptファイルが該当します。

ディレクトリ構成の例を以下に示します。
```
project/
├── manage.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app1/
│   ├── migrations/
│   ├── static/
│   │   ├── app1/
│   │   │   ├── css/
│   │   │   │   └── main.css
│   │   │   └── js/
│   │   │       └── script.js
│   │   └── common/
│   │       ├── css/
│   │       │   └── base.css
│   │       └── js/
│   │           └── common.js
│   ├── templates/
│   └── ...
├── app2/
│   ├── migrations/
│   ├── static/
│   │   ├── app2/
│   │   │   ├── css/
│   │   │   └── js/
│   │   └── common/
│   └── ...
└── ...
```

このようなディレクトリ構成を採用することで、静的ファイルの管理が容易になります。静的ファイルがどのアプリケーションに属するかが明確になるため、開発者が必要なファイルを素早く見つけることができます。

参考ブログ記事：
- [django公式ドキュメント - managing static files　(英語)](https://docs.djangoproject.com/en/3.2/howto/static-files/)
- [djangoアプリケーション開発で使う静的ファイルの配置方法](https://qiita.com/felyce/items/2ddb3da9a1f61be0ebc5)

## cssファイルの読み込み方法とは？

cssファイルは、htmlテンプレート内で`link`要素を使用して読み込むことができます。djangoでは、静的ファイルを読み込むための専用のテンプレートタグ`{% static %}`を使用します。

具体的な手順は以下の通りです。
1. htmlテンプレート内で、`{% load static %}`というタグを使用して静的ファイルの読み込み準備をする。
2. `link`要素を使用し、cssファイルを読み込む。この際、`href`属性に`{% static 'appname/path/to/cssfile.css' %}`という形式で指定する。

以下にサンプルコードを示します。
```html
{% load static %}
<!doctype html>
<html>
<head>
    <title>my web page</title>
    <link rel="stylesheet" href="{% static 'appname/css/style.css' %}">
</head>
<body>
    <!-- ページのコンテンツ -->
</body>
</html>
```

`{% static 'appname/css/style.css' %}`という部分で、静的ファイルのパスを指定しています。`appname`はアプリケーション名に、`css/style.css`はcssファイルの相対パスにそれぞれ置き換えてください。

参考ブログ記事：
- [django公式ドキュメント - managing static files　(英語)](https://docs.djangoproject.com/en/3.2/howto/static-files/)
- [djangoでcssを読み込む方法【初心者向け】](https://note.nkmk.me/python-django-static-file-css-howto/)

## javascriptファイルの読み込み方法とは？

javascriptファイルもcssファイルと同様に、htmlテンプレート内で`script`要素を使用して読み込むことができます。djangoでは、静的ファイルを読み込むためのテンプレートタグ`{% static %}`を使用します。

具体的な手順は以下の通りです。
1. htmlテンプレート内で、`{% load static %}`というタグを使用して静的ファイルの読み込み準備をする。
2. `script`要素を使用し、javascriptファイルを読み込む。この際、`src`属性に`{% static 'appname/path/to/script.js' %}`という形式で指定する。

以下にサンプルコードを示します。
```html
{% load static %}
<!doctype html>
<html>
<head>
    <title>my web page</title>
</head>
<body>
    <!-- ページのコンテンツ -->
    <script src="{% static 'appname/js/script.js' %}"></script>
</body>
</html>
```

`{% static 'appname/js/script.js' %}`という部分で、静的ファイルのパスを指定しています。`appname`はアプリケーション名に、`js/script.js`はjavascriptファイルの相対パスにそれぞれ置き換えてください。

参考ブログ記事：
- [django公式ドキュメント - managing static files　(英語)](https://docs.djangoproject.com/en/3.2/howto/static-files/)
- [djangoでjavascriptを読み込む方法【初心者向け】](https://note.nkmk.me/python-django-static-file-js-howto/)

## 静的ファイルのキャッシュの扱い方とは？

静的ファイルのキャッシュは、webサイトのパフォーマンス向上やユーザーエクスペリエンスの向上に役立ちます。キャッシュされた静的ファイルはクライアントのブラウザに保存され、次回以降のアクセス時に再ダウンロードせずに利用することができます。そのため、読み込み速度が向上し、ユーザーの待ち時間が低減されます。

djangoでは、静的ファイルのキャッシュの扱い方を設定するためのオプションが用意されています。`settings.py`ファイルの中にある`staticfiles_storage`という設定を調整することで、キャッシュの有効化や設定のカスタマイズが可能です。

例えば、`django.contrib.staticfiles.storage.manifeststaticfilesstorage`というストレージクラスを使用すると、静的ファイルの名前をハッシュ値に変換し、ファイルの内容が変更された場合にのみ新しいファイル名として読み込まれます。これにより、ブラウザのキャッシュが古いファイルを使用することを防ぐことができます。

キャッシュによるパフォーマンス向上の効果は大きいため、本番環境ではキャッシュの有効化を検討することをおすすめします。

参考ブログ記事：
- [django公式ドキュメント - managing static files　(英語)](https://docs.djangoproject.com/en/3.2/howto/static-files/)
- [djangoで静的ファイルのキャッシュを有効化する方法](https://qiita.com/felyce/items/e4945fed265d54dcdc5e)

　

## Django 関連のまとめ
https://hack-note.com/summary/django-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

