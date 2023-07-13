【Laravel】where句を使ってデータを検索する方法
php,laravel,where
php-laravel-where

こんにちは。今回は、Laravel初心者に向けて、where句を使ってデータを検索する方法について解説します。

## where句とは

where句は、SQLのSELECT文において、指定した条件に合致するレコードのみを取得するための条件式です。Laravelにも同様の機能があり、Eloquent ORMを使ってデータベースからデータを取得する際に利用することができます。

## where句の使い方

Laravelにおいて、where句を使ってデータを取得するには、以下のように記述します。

```php
$users = DB::table('users')
                ->where('name', '=', 'John')
                ->get();
```

上記の例では、usersテーブルからnameがJohnのレコードを取得しています。whereメソッドの第一引数にはカラム名、第二引数には比較演算子、第三引数には比較する値を指定します。また、複数の条件を指定する場合は、andやorを使って連結することができます。

```php
$users = DB::table('users')
                ->where('name', '=', 'John')
                ->orWhere('name', '=', 'Jane')
                ->get();
```

上記の例では、nameがJohnまたはJaneのレコードを取得しています。

## Eloquent ORMを使ったwhere句の使い方

Eloquent ORMを使ってwhere句を利用する場合は、Modelクラスのwhereメソッドを使います。以下のように記述します。

```php
$users = User::where('name', '=', 'John')->get();
```

上記の例では、UserモデルからnameがJohnのレコードを取得しています。複数の条件を指定する場合は、以下のように記述します。

```php
$users = User::where('name', '=', 'John')
                ->orWhere('name', '=', 'Jane')
                ->get();
```

## サンプルコード

以下は、Eloquent ORMを使ってwhere句を利用する例です。Userモデルに対して、ageカラムが30以上のレコードを取得するコードです。

```php
$users = User::where('age', '>=', 30)->get();
```

また、以下は、複数の条件を指定する例です。Userモデルに対して、nameがJohnかつageが30以上のレコードを取得するコードです。

```php
$users = User::where('name', '=', 'John')
                ->where('age', '>=', 30)
                ->get();
```

## 注意点

where句を使ってデータを取得する際には、セキュリティ上の問題に注意する必要があります。入力値をそのままクエリに埋め込むと、SQLインジェクション攻撃を受ける可能性があります。そのため、入力値を適切にバリデーションし、プレースホルダを使ってクエリを組み立てるようにしましょう。

## まとめ

Laravelにおいて、where句を使ってデータを検索する方法について解説しました。where句を使うことで、指定した条件に合致するレコードのみを取得することができます。また、複数の条件を指定することも可能です。ただし、セキュリティ上の問題に注意して、入力値を適切にバリデーションし、プレースホルダを使ってクエリを組み立てるようにしましょう。

　

## Laravel 関連のまとめ
https://hack-note.com/summary/laravel-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

