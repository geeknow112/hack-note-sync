【django】テンプレートエンジンを使ったwebページの動的生成方法
python,django
django-template.md

## djangoのテンプレートエンジンとは？

djangoは、pythonで開発されたwebアプリケーションフレームワークであり、テンプレートエンジンを使用して動的なwebページを生成することができます。テンプレートエンジンとは、可読性の高いテンプレートを作成し、動的に変化するコンテンツを埋め込むことができる仕組みのことです。テンプレートエンジンを使用することにより、htmlコードを直接書く必要がなくなり、pythonのコードとhtmlを簡潔に組み合わせることができます。これにより、webページの開発効率が向上し、保守性も高まります。

参考記事：
- [django documentation: templates](https://docs.djangoproject.com/en/3.2/topics/templates/)
- [django templates: beginner's guide](https://ntucker.me/django-templates-beginners-guide/)

## テンプレートを使ったwebページの基本的な構成と書き方

テンプレートを使ったwebページの基本的な構成は以下のようになります。

1. テンプレートファイルの作成
2. テンプレート内での変数やタグの使用
3. ビューでテンプレートをレンダリングして表示

まず、テンプレートファイルを作成します。テンプレートファイルはhtmlファイルとして保存され、拡張子は`.html`となります。テンプレート内で使用する変数やタグは、波括弧`{{ }}`で囲みます。

例えば、以下のようなテンプレートファイルを作成します。

```html
<!doctype html>
<html>
<head>
  <title>{{ title }}</title>
</head>
<body>
  <h1>{{ heading }}</h1>
  <p>{{ content }}</p>
</body>
</html>
```

参考記事：
- [django documentation: templates](https://docs.djangoproject.com/en/3.2/topics/templates/)
- [django templates: beginner's guide](https://ntucker.me/django-templates-beginners-guide/)

## テンプレート内での変数の扱い方とは？

テンプレート内で変数を扱う方法は非常にシンプルです。テンプレート内で使用する変数は、ビューで渡されたコンテキストに含まれています。変数を表示するには、波括弧`{{ }}`で囲みます。

例えば、ビューで以下のように変数をコンテキストに追加します。

```python
from django.shortcuts import render

def my_view(request):
    context = {
        'title': 'my page',
        'heading': 'welcome to my website!',
        'content': 'this is the content of my page.',
    }
    return render(request, 'my_template.html', context)
```

この場合、テンプレート内で`{{ title }}`を使用すると`my page`と表示されます。

参考記事：
- [django documentation: templates](https://docs.djangoproject.com/en/3.2/topics/templates/)
- [django templates: beginner's guide](https://ntucker.me/django-templates-beginners-guide/)

## フィルターを使ったテンプレートのデータ加工方法とは？

テンプレート内でのデータの加工や書式設定には、フィルターを使用することができます。フィルターは、変数にパイプ`|`を追加し、その後にフィルター名を記述することで使用します。

例えば、以下のようにフィルターを使用してデータを加工することができます。

```html
<p>{{ content | upper }}</p>
<p>{{ date | date:"y/m/d" }}</p>
```

上記の例では、文字列を大文字に変換する`upper`フィルターと、日付を指定した形式で表示する`date`フィルターを使用しています。

参考記事：
- [django documentation: template filters](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#ref-templates-builtins-filters)
- [django templates: beginner's guide](https://ntucker.me/django-templates-beginners-guide/)

## テンプレート内での条件分岐と繰り返し処理の書き方とは？

テンプレート内での条件分岐や繰り返し処理は、`{% %}`タグを使用して記述します。条件分岐には`if`タグを、繰り返し処理には`for`タグを使用します。

例えば、以下のように条件分岐を行うことができます。

```html
{% if age >= 20 %}
  <p>you are an adult.</p>
{% else %}
  <p>you are underage.</p>
{% endif %}
```

また、以下のように繰り返し処理を行うことができます。

```html
<ul>
  {% for fruit in fruits %}
    <li>{{ fruit }}</li>
  {% endfor %}
</ul>
```

上記の例では、`fruits`というリストの要素を順に表示しています。

参考記事：
- [django documentation: template tags and filters](https://docs.djangoproject.com/en/3.2/topics/templates/#tags-and-filters)
- [django templates: beginner's guide](https://ntucker.me/django-templates-beginners-guide/)

## テンプレートの継承を使ったwebページの共通部分の効率的な管理方法

テンプレートの継承を使用することで、webページの共通部分を効率的に管理することができます。継承を使用すると、共通部分を親テンプレートとして定義し、子テンプレートでその共通部分を利用することができます。これにより、共通のレイアウトやナビゲーションメニューなどを共有しながら、個別のコンテンツ部分を柔軟に設定することができます。

例えば、以下のように親テンプレートを作成します。

```html
<!doctype html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
</head>
<body>
  <header>
    <nav>
      <!-- ナビゲーションメニュー -->
    </nav>
  </header>

  <main>
    {% block content %}
    {% endblock %}
  </main>

  <footer>
    <!-- フッター部分 -->
  </footer>
</body>
</html>
```

そして、子テンプレートで`{% extends %}`タグを使用して親テンプレートを継承します。

```html
{% extends "base.html" %}

{% block title %}my page{% endblock %}

{% block content %}
  <h1>welcome to my website!</h1>
  <p>this is the content of my page.</p>
{% endblock %}
```

上記の例では、子テンプレートでタイトルとコンテンツ部分を定義しています。

参考記事：
- [django documentation: template inheritance](https://docs.djangoproject.com/en/3.2/topics/templates/#id1)
- [django templates: beginner's guide](https://ntucker.me/django-templates-beginners-guide/)

以上、本記事ではdjangoのテンプレートエンジンを使ったwebページの動的生成方法について解説しました。初心者エンジニアの方々がdjangoを学ぶ上での参考になれば幸いです。

## 参考記事

- [django documentation: templates](https://docs.djangoproject.com/en/3.2/topics/templates/)
- [django templates: beginner's guide](https://ntucker.me/django-templates-beginners-guide/)

　

## Django 関連のまとめ
https://hack-note.com/summary/django-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

