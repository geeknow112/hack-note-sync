【django】ルーティングとurl設計について
python,django
django-routing

## はじめに: ルーティングとurl設計の重要性
こんにちは。今回は、djangoについて初心者エンジニアに向けて、ルーティングとurl設計について解説します。ルーティングとは、ユーザーからのリクエストをどのビュー関数に紐付けるかを指定する仕組みのことです。url設計とは、urlの形式やパターンをどのように決めるかということです。

ルーティングとurl設計は、ウェブアプリケーションの設計において非常に重要な要素です。正しいurl設計とルーティングの設定により、ユーザーが直感的にアクセスできる独自のurl構造を作ることができます。また、柔軟なurl設計により、将来的な機能追加や変更に対応することも容易になります。

では、djangoにおけるルーティングの仕組みから見ていきましょう。

## djangoにおけるルーティングの仕組み
djangoでは、ルーティングはurlconfと呼ばれるモジュールによって管理されます。urlconfは、urlパターンとビュー関数またはビュークラスを紐付けるための設定が記述されたpythonのモジュールです。

urlconfは、urls.pyというファイル名でプロジェクトのルートディレクトリに配置します。通常、アプリケーションごとにurls.pyファイルを作成し、それらをプロジェクトのurls.pyからインクルードすることで、ルーティングを設定します。

urlconfでは、urlパターンを正規表現で定義し、そのパターンに一致するurlがリクエストされた場合に、指定されたビュー関数またはビュークラスを実行します。urlconfは、リクエストされたurlを順番に比較し、最初に一致するパターンに対応するビューを実行します。

以下のコードは、urlconfの一部の例です。

```python
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:pk>/', views.article_detail),
]
```

この例では、urlの/articles/にアクセスした場合には、views.article_list関数が実行されます。また、urlの/articles/1/のように記事のidが指定された場合には、views.article_detail関数が実行されます。

## urlパターンの定義と設定
urlconfでurlパターンを定義する際には、正規表現を用いることができます。正規表現を使用することで、柔軟なurlのマッチングが可能となります。

urlパターンは、path関数の第一引数として指定します。第一引数には、urlのパターンを正規表現で指定します。例えば、`path('articles/<int:pk>/', views.article_detail)`というパスは、/articles/1/というurlに一致します。

正規表現では、特殊な文字（.や*など）や角括弧([と])を使用することができ、パターンの一部を変数として扱うこともできます。例えば、`path('articles/<int:pk>/', views.article_detail)`というパスでは、<int:pk>の部分が記事のidとしてビュー関数に渡されます。

## urlパターンとビュー関数の連携
urlパターンとビュー関数を連携するためには、urlconfでビュー関数を指定する必要があります。ビュー関数は、リクエストを受けて処理を行い、レスポンスを返す役割を果たします。

ビュー関数は、通常、views.pyというファイルに定義し、urlconfではviewsモジュールから関数をインポートして使用します。以下は、views.pyに定義されたビュー関数の例です。

```python
from django.shortcuts import render
from django.http import httpresponse

def article_list(request):
    # 記事一覧を取得する処理
    articles = article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, pk):
    # 指定された記事を取得する処理
    article = article.objects.get(pk=pk)
    return render(request, 'article_detail.html', {'article': article})
```

ビュー関数では、リクエストを受けて必要なデータを取得し、htmlテンプレートに渡してレスポンスを返します。レスポンスは、render関数を使用してhtmlテンプレートをレンダリングすることで生成します。

## 名前付きurlとリバースルックアップ
djangoでは、urlconfで定義したurlパターンに名前をつけることができます。これにより、ビュー関数へのリンクやリダイレクトなどが容易になります。

名前付きurlを使用するには、path関数のname引数に名前を指定します。例えば、`path('articles/', views.article_list, name='article_list')`というパスは、名前付きurl "article_list" として使用することができます。

名前付きurlをビュー関数で使用する場合には、reverse関数を使用します。reverse関数は、urlconfで定義したパターン名を引数として受け取り、urlを逆引きする役割を果たします。以下は、ビュー関数内で名前付きurlを使用する例です。

```python
from django.shortcuts import reverse
from django.http import httpresponse

def index(request):
    article_list_url = reverse('article_list')
    return httpresponse(f"<a href='{article_list_url}'>article list</a>")
```

この例では、ビュー関数内でreverse関数を使用して名前付きurl "article_list" のurlを取得し、htmlレスポンスとして返しています。

## わかりやすく効果的なurl設計のポイント
最後に、わかりやすく効果的なurl設計のポイントをいくつか紹介します。

1. リソースを表す名詞や名詞句を使用する
2. 複数のリソースを持つ場合には、階層的なurl構造を使用する
3. urlのパラメータは、できるだけ明示的な名前を使用する
4. 必要に応じて、クエリパラメータを使用する

以上が、djangoにおけるルーティングとurl設計の基本的な内容です。url設計は、ウェブアプリケーションのユーザーエクスペリエンスに大きな影響を与える重要な要素であるため、ぜひ理解して活用してください。

参考記事:
- [the django urlconf](https://docs.djangoproject.com/en/3.2/topics/http/urls/)
- [url dispatcher](https://docs.djangoproject.com/en/3.2/topics/http/urls/#url-dispatcher)

　

## Django 関連のまとめ
https://hack-note.com/summary/django-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

