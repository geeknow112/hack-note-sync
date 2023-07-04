【django】インストール方法と基本的な使い方
python,django
django-install

## djangoのインストール方法
djangoをインストールするためには、まずpythonのインストールが必要です。pythonはプログラミング言語であり、djangoはpythonで書かれているため、pythonのインストールが先に必要です。

pythonの公式サイト(https://www.python.org)から最新の安定版をダウンロードし、インストールします。ダウンロードしたファイルを実行し、指示に従ってpythonをインストールしてください。

pythonのインストールが完了したら、次にdjangoをインストールします。ターミナルまたはコマンドプロンプトを開き、以下のコマンドを入力します。

```
$ pip install django
```

これにより、djangoがインストールされます。インストールが完了したら、以下のコマンドを入力してバージョンを確認しましょう。

```
$ django-admin --version
```

以上でdjangoのインストールは完了です。

参考記事： 
- [djangoのインストールとセットアップ方法](https://qiita.com/okoppe8/items/178357bdaedad8d01cc3)
- [djangoを始めよう！pythonでwebアプリケーション開発入門](https://www.sejuku.net/blog/24913)

## djangoプロジェクトの作成と構成
djangoのプロジェクトを作成するには、以下のコマンドを入力します。

```
$ django-admin startproject myproject
```

`myproject`はプロジェクト名であり、任意の名前を指定できます。このコマンドを実行すると、`myproject`という名前のフォルダが作成され、djangoのプロジェクトの骨格が自動的に生成されます。

プロジェクトの構造は以下のようになります。

```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

- `manage.py`: djangoに関連する様々な操作を実行するためのコマンドラインツールです。
- `myproject`: プロジェクトの設定が含まれるパッケージです。
    - `__init__.py`: パッケージであることを示すための空のファイルです。
    - `settings.py`: プロジェクトの設定を管理するファイルです。
    - `urls.py`: urlのパターンとビューの対応を設定するファイルです。
    - `asgi.py`: asgi（asynchronous server gateway interface）を使用するためのファイルです。
    - `wsgi.py`: wsgi（web server gateway interface）を使用するためのファイルです。

参考記事：
- [djangoをはじめよう！作成したプロジェクトの構成を解説](https://toukei-lab.com/django-project-structure/)
- [djangoについて語る – 1. djangoのプロジェクト構成](https://www.django-ninjas.com/blog/django-project-structure)

## djangoアプリケーションの作成と設定
djangoでは、複数のアプリケーションを1つのプロジェクト内で管理することができます。アプリケーションを作成するには、以下のコマンドを入力します。

```
$ python manage.py startapp myapp
```

`myapp`はアプリケーション名であり、任意の名前を指定できます。このコマンドを実行すると、`myapp`という名前のフォルダが作成され、基本的なアプリケーションの骨格が自動的に生成されます。

アプリケーションの構造は以下のようになります。

```
myapp/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

- `__init__.py`: パッケージであることを示すための空のファイルです。
- `admin.py`: 管理サイトでのモデルの登録やカスタマイズを行うファイルです。
- `apps.py`: アプリケーションの設定を管理するファイルです。
- `migrations/`: データベースのマイグレーションファイルが格納されるディレクトリです。
    - `__init__.py`: パッケージであることを示すための空のファイルです。
- `models.py`: データベースのモデルを定義するファイルです。
- `tests.py`: テストコードを記述するためのファイルです。
- `views.py`: ビュー（画面）の処理を記述するファイルです。

アプリケーションをプロジェクトに追加するには、プロジェクトの`settings.py`ファイルの`installed_apps`リストに追加する必要があります。

参考記事：
- [djangoをはじめよう！新しいアプリケーションを作ってみよう](https://toukei-lab.com/django-startapp-create-app/)
- [djangoで新しいアプリケーションを作成する方法](https://www.django-ninjas.com/blog/how-to-create-new-application-in-django)

## ビュー、url、テンプレートの基本
djangoでは、ビュー（画面の表示やデータの処理を行うコード）、url（アクセスされたurlに対してどのビューを表示するかを設定）、テンプレート（htmlや表示データの構造を定義するファイル）を組み合わせることでwebアプリケーションを構築します。

### ビューの作成
ビューは`views.py`ファイルに作成し、関数またはクラスとして定義します。以下は、簡単なビューの例です。

```python
from django.http import httpresponse

def hello(request):
    return httpresponse("hello, world!")
```

### urlの設定
urlを設定するには、`urls.py`ファイルを編集します。以下は、先ほどのビューをurlに紐付ける例です。

```python
from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]
```

- `path()`関数によって、urlパターンとビューの関連付けが行われます。
- `'hello/'`はurlパターンであり、`http://example.com/hello/`でアクセスされた場合に`views.hello`ビューが表示されるようになります。
- `name='hello'`はビューに名前を付けるためのものであり、テンプレートなどで使用することができます。

### テンプレートの作成
テンプレートは、htmlや表示データの構造を定義するファイルです。以下は、簡単なテンプレートの例です。

```html
<!doctype html>
<html>
<head>
    <title>hello, django!</title>
</head>
<body>
    <h1>{{ message }}</h1>
</body>
</html>
```

`{{ message }}`はテンプレート内で変数を表示するためのものであり、ビューから渡されたデータを表示することができます。

参考記事：
- [djangoビューの作成とurlの設定方法](https://toukei-lab.com/django-view-url/)
- [djangoのテンプレートエンジンでhtmlテンプレートを作成する方法](https://www.django-ninjas.com/blog/how-to-create-html-templates-in-django)

## データベースとモデルの基本
djangoでは、データベースとモデルを使用してデータの永続化を行います。モデルはデータベースのテーブルとして定義され、データの操作やクエリを行うためのインターフェースを提供します。

### データベースの設定
デフォルトでは、djangoはsqliteという軽量なデータベースを使用します。他のデータベース（mysql、postgresql、oracleなど）を使用する場合は、`settings.py`ファイルの`databases`設定を変更します。

### モデルの定義
モデルは`models.py`ファイルで定義されます。以下は、簡単なモデルの例です。

```python
from django.db import models

class book(models.model):
    title = models.charfield(max_length=100)
    author = models.charfield(max_length=100)
    publication_date = models.datefield()
```

- `models.model`を継承することで、モデルを定義します。
- `charfield`は文字列フィールドを表し、`max_length`で最大文字数を指定します。
- `datefield`は日付フィールドを表します。

### マイグレーション
モデルを変更した場合、データベースに対してマイグレーションを行う必要があります。マイグレーションは、モデルの変更内容をデータベースに反映するための手順です。

マイグレーションを作成するには、以下のコマンドを入力します。

```
$ python manage.py makemigrations
```

このコマンドによって、現在のモデルの状態と前回のマイグレーションの状態を比較し、必要な変更を検出します。

マイグレーションを適用するには、以下のコマンドを入力します。

```
$ python manage.py migrate
```

このコマンドによって、データベースにマイグレーションが適用され、モデルの変更が反映されます。

参考記事：
- [djangoのデータベース設定とモデルの定義方法](https://toukei-lab.com/django-database-model/)
- [djangoにおけるデータベースとは？モデルの基礎知識](https://www.django-ninjas.com/blog/django-database-model)

　

## Django 関連のまとめ
https://hack-note.com/summary/django-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

