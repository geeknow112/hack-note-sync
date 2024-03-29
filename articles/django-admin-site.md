【django】管理サイトの使い方：データの追加や編集、削除方法
python,django
django-admin-site

## djangoの管理サイトの概要と設定方法

こんにちは。今回は、djangoについて初心者エンジニアに向けて、djangoの管理サイトの使い方についてご紹介します。djangoは、pythonで開発されたwebアプリケーションフレームワークであり、データベースの管理やcrud操作を簡単に行うことができます。djangoの管理サイトは、データの追加や編集、削除などの操作をweb上で行うことができる便利なツールです。

まずは、djangoの管理サイトを使うための設定方法からご説明します。設定方法は以下の手順で行います。

1. `settings.py`ファイルを開きます。
2. `installed_apps`リストに、`django.contrib.admin`を追加します。
3. `urls.py`ファイルを開き、`admin`というurlパターンを追加します。
4. ターミナルで`python manage.py migrate`コマンドを実行して、データベースをマイグレーションします。
5. ターミナルで`python manage.py createsuperuser`コマンドを実行して、管理者ユーザーを作成します。

以上の手順を実行することで、djangoの管理サイトが使えるようになります。次に、管理サイトにモデルを登録する方法について見ていきましょう。

## モデルの作成と管理サイトへの登録方法

モデルは、データベースのテーブルを定義するためのクラスです。モデルを作成し、管理サイトに登録する手順は以下の通りです。

1. `models.py`ファイルを開き、モデルクラスを定義します。
```
from django.db import models

class blog(models.model):
    title = models.charfield(max_length=100)
    content = models.textfield()
    created_at = models.datetimefield(auto_now_add=true)
```
上記の例では、ブログ記事を管理するためのモデルクラスを定義しています。

2. `admin.py`ファイルを開き、作成したモデルを管理サイトに登録します。
```
from django.contrib import admin
from .models import blog

admin.site.register(blog)
```
上記の例では、`blog`モデルを管理サイトに登録しています。

これで、作成したモデルが管理サイトで操作できるようになりました。次に、管理サイトでのデータの閲覧と検索方法について見ていきましょう。

## 管理サイトでのデータの閲覧と検索方法

管理サイトでは、登録したモデルのデータを閲覧することができます。また、検索機能を使って特定のデータを絞り込むこともできます。以下の手順でデータを閲覧または検索することができます。

1. ブラウザで管理サイトにアクセスします。
2. ログイン画面が表示されるので、作成した管理者ユーザーでログインします。
3. メイン画面に表示されているモデルの一覧から、閲覧したいモデルを選択します。
4. 一覧画面が表示されるので、データを閲覧したり、検索条件を入力して絞り込んだりすることができます。

以上で、管理サイトでのデータの閲覧と検索が完了しました。次に、管理サイトでのデータの追加と保存方法について見ていきましょう。

## 管理サイトでのデータの追加と保存方法

管理サイトでは、データの追加と保存を簡単に行うことができます。以下の手順でデータの追加と保存を行います。

1. ブラウザで管理サイトにアクセスします。
2. ログイン画面が表示されるので、作成した管理者ユーザーでログインします。
3. メイン画面に表示されているモデルの一覧から、新しく追加したいモデルを選択します。
4. モデルの詳細画面が表示されるので、追加したいデータを入力します。
5. 入力が完了したら、保存ボタンをクリックしてデータを保存します。

上記の手順で、簡単にデータの追加と保存を行うことができます。次に、管理サイトでのデータの編集と更新方法について見ていきましょう。

## 管理サイトでのデータの編集と更新方法

管理サイトでは、登録したデータを編集し、更新することができます。以下の手順でデータの編集と更新を行います。

1. ブラウザで管理サイトにアクセスします。
2. ログイン画面が表示されるので、作成した管理者ユーザーでログインします。
3. メイン画面に表示されているモデルの一覧から、編集したいデータを選択します。
4. データの詳細画面が表示されるので、編集したい項目を編集します。
5. 編集が完了したら、保存ボタンをクリックしてデータを更新します。

以上の手順で、簡単にデータの編集と更新を行うことができます。最後に、管理サイトでのデータの削除方法について見ていきましょう。

## 管理サイトでのデータの削除方法

管理サイトでは、登録したデータを削除することができます。以下の手順でデータの削除を行います。

1. ブラウザで管理サイトにアクセスします。
2. ログイン画面が表示されるので、作成した管理者ユーザーでログインします。
3. メイン画面に表示されているモデルの一覧から、削除したいデータを選択します。
4. データの詳細画面が表示されるので、削除ボタンをクリックしてデータを削除します。

以上の手順で、簡単にデータの削除を行うことができます。

以上で、djangoの管理サイトの使い方についてご紹介しました。初心者の方にも分かりやすいように解説を行いましたが、もし分からない箇所があれば、公式ドキュメントや参考記事を参照してください。djangoの管理サイトは開発効率を向上させる便利なツールですので、ぜひ活用してみてください。

参考記事：
- [django公式ドキュメント - adminサイト](https://docs.djangoproject.com/ja/3.2/ref/contrib/admin/)
- [qiita - djangoの管理サイト（admin）の使い方](https://qiita.com/okoppe8/items/4191fd754e5d3d328e73)

　

## Django 関連のまとめ
https://hack-note.com/summary/django-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

