【django】プラグイン開発の応用テクニック：カスタム管理画面やapi拡張を実現しよう
django,python
django-plugin-advanced-techniques

## カスタム管理画面の作成と拡張

こんにちは。今回は、djangoについて初心者エンジニアに向けて、プラグイン開発の応用テクニックについてご紹介します。

djangoは、pythonで開発された人気のあるwebアプリケーションフレームワークであり、多くのウェブサイトやアプリケーションの開発に利用されています。djangoの強力な機能の1つに、管理画面のカスタマイズや拡張があります。この機能を使うことで、データベースのモデルの操作や表示方法をカスタマイズできるだけでなく、独自のapiエンドポイントを追加することも可能です。

djangoの管理画面は、デフォルトではシンプルな操作性がありますが、特定の要件やデザインに合わせてカスタマイズすることもできます。例えば、自分のアプリケーションに関連するモデルだけを表示する、特定のフィールドを非表示にする、フィールドの値を変換して表示する、などのカスタマイズが可能です。

以下では、実際のコードを用いてカスタム管理画面の作成と拡張の手法をご紹介していきます。

## django管理画面のカスタムモデル表示とフィールド設定

まず、管理画面のカスタムモデル表示とフィールド設定について見ていきましょう。djangoの管理画面では、`admin.py`というファイルを作成し、管理するモデルクラスを登録することで、モデルの一覧や詳細ビューが表示されるようになります。

例えば、以下のような`models.py`ファイルがあるとします。

```python
from django.db import models

class book(models.model):
    title = models.charfield(max_length=100)
    author = models.charfield(max_length=100)
    publication_date = models.datefield()
```

この場合、`admin.py`ファイルに以下のように記述することで、管理画面での表示や操作方法をカスタマイズすることができます。

```python
from django.contrib import admin
from .models import book

class bookadmin(admin.modeladmin):
    list_display = ('title', 'author', 'publication_date')

admin.site.register(book, bookadmin)
```

上記の例では、`book`モデルを管理画面に登録し、表示するフィールドとして`title`、`author`、`publication_date`を指定しています。これにより、管理画面での一覧ビューおよび詳細ビューに指定したフィールドが表示されるようになります。

## 管理画面のアクションとフィルタのカスタマイズ

次に、管理画面のアクションとフィルタのカスタマイズについて見ていきましょう。djangoの管理画面では、データベースのモデルに対して一括で操作を行うためのアクションや、絞り込んで表示するためのフィルタを設定することができます。

例えば、以下のような`admin.py`ファイルがあるとします。

```python
from django.contrib import admin
from .models import book

class bookadmin(admin.modeladmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ['author']
    actions = ['publish_books']

    def publish_books(self, request, queryset):
        queryset.update(published=true)

admin.site.register(book, bookadmin)
```

上記の例では、`book`モデルの詳細ビューに`title`、`author`、`publication_date`のフィールドが表示されるだけでなく、`author`を基準にフィルタをかけることができます。

また、`actions`パラメータに`publish_books`というアクションを追加し、選択された書籍の`published`フィールドを`true`に更新することができます。

## 管理画面の外観とテーマの変更方法

次に、管理画面の外観とテーマの変更方法について見ていきましょう。djangoの管理画面では、デフォルトの外観をカスタマイズするだけでなく、独自のテーマを適用することもできます。

例えば、以下のような`admin.py`ファイルがあるとします。

```python
from django.contrib import admin
from .models import book

class customadminsite(admin.adminsite):
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        urls += [
            path('my_custom_view/', self.admin_view(self.my_custom_view))
        ]
        return urls

    def my_custom_view(self, request):
        # 独自のビューを定義する処理
        pass

custom_site = customadminsite(name='custom_admin')
custom_site.register(book)

admin.site = custom_site
```

上記の例では、`adminsite`クラスを継承した`customadminsite`クラスを作成し、`get_urls`メソッドをオーバーライドして、独自のビューを追加することができます。

また、`adminsite`クラスのサブクラスを作成することで、テーマをカスタマイズすることもできます。例えば、以下のように`customadminsite`クラスを作成して、デフォルトのテーマをカスタマイズすることができます。

```python
from django.contrib import admin
from django.contrib.admin.sites import adminsite
from myapp.models import book

class customadminsite(adminsite):
    site_title = 'my custom admin'
    site_header = 'my custom admin'
    index_title = 'welcome to my custom admin'
    site_url = '/my_custom_admin/'

custom_admin_site = customadminsite(name='custom_admin')
custom_admin_site.register(book)

admin.site = custom_admin_site
```

上記の例では、`customadminsite`クラスを作成し、`site_title`、`site_header`、`index_title`、`site_url`などのプロパティをオーバーライドして、管理画面のテーマをカスタマイズしています。

## django rest frameworkを使用したapiの拡張

次に、django rest frameworkを使用したapiの拡張について見ていきましょう。django rest frameworkを使うことで、djangoの管理画面に加えて独自のapiエンドポイントを作成することができます。

例えば、以下のような`views.py`ファイルがあるとします。

```python
from rest_framework import viewsets
from .serializers import bookserializer
from .models import book

class bookviewset(viewsets.modelviewset):
    queryset = book.objects.all()
    serializer_class = bookserializer
```

上記の例では、`rest_framework`モジュールを使って、`book`モデルに対するapiエンドポイントを作成しています。`modelviewset`クラスを継承した`bookviewset`クラスでは、`queryset`にモデルのデータを指定し、`serializer_class`にシリアライザのクラスを指定しています。

次に、以下のような`serializers.py`ファイルを作成します。

```python
from rest_framework import serializers
from .models import book

class bookserializer(serializers.modelserializer):
    class meta:
        model = book
        fields = ('title', 'author', 'publication_date')
```

上記の例では、`book`モデルに対するシリアライザのクラスを定義しています。`meta`クラスの`model`にモデルクラスを、`fields`に表示させるフィールドを指定しています。

最後に、以下のような`urls.py`ファイルを作成します。

```python
from django.urls import include, path
from rest_framework import routers
from .views import bookviewset

router = routers.defaultrouter()
router.register(r'books', bookviewset)

urlpatterns = [
    path('', include(router.urls))
]
```

上記の例では、`routers`モジュールを使ってルーターを作成し、`bookviewset`を`books`というパスに登録しています。これにより、`/books/`にアクセスすると、`book`モデルのデータを表示するapiエンドポイントが利用できるようになります。

## カスタムapiエンドポイントの作成と認証の実装

最後に、カスタムapiエンドポイントの作成と認証の実装について見ていきましょう。djangoでは、独自のapiエンドポイントを簡単に作成することができます。

例えば、以下のような`views.py`ファイルがあるとします。

```python
from django.http import jsonresponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def custom_api_view(request):
    if request.method == 'get':
        data = {
            'message': 'hello, world!'
        }
        return jsonresponse(data)
```

上記の例では、`custom_api_view`という関数ベースのapiビューを作成しています。`csrf_exempt`デコレータを使うことで、csrfトークンの検証を無効化しています。`get`メソッドでアクセスされた場合には、`message`というキーで`hello, world!`というテキストを返すようにしています。

このように、djangoを使うことで簡単にカスタム管理画面やapi拡張を実現することができます。初心者の方でも、djangoの強力な機能を活用して、自分のアプリケーションをさらにパワーアップさせましょう。

それでは、本記事を参考にしてdjangoのプラグイン開発の応用テクニックを活用してみてください。

参考記事：
- [django admin cookbook](https://books.agiliq.com/projects/django-admin-cookbook/en/latest/)
- [django rest framework documentation](https://www.django-rest-framework.org/)

　

## 【Django】関連のまとめ
https://hack-note.com/summary/django-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

