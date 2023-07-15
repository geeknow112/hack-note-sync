【Laravel】データベース操作をする方法とEloquent ORMの基本
php,laravel,eloquent
php-laravel-eloquent

こんにちは。今回は、Laravel初心者に向けて、データベース操作の基本とEloquent ORMについて解説します。

## データベース操作の基本

Laravelでは、データベース操作にはQueryBuilderとEloquent ORMの2つの方法があります。QueryBuilderは、SQL文を直接記述してデータベースにアクセスする方法で、Eloquent ORMは、オブジェクト指向的にデータベースにアクセスする方法です。まずは、QueryBuilderを使ったデータベース操作の基本から解説します。

### データの取得

データの取得には、以下のように記述します。

```php
$users = DB::table('users')->get();
```

上記の例では、usersテーブルの全てのレコードを取得しています。getメソッド以外にも、firstメソッドやvalueメソッドなど、取得方法は様々あります。詳細は公式ドキュメントを参照してください。

### データの挿入

データの挿入には、以下のように記述します。

```php
DB::table('users')->insert(
    ['name' => 'John Doe', 'email' => 'johndoe@example.com']
);
```

上記の例では、usersテーブルに、nameカラムに'John Doe'、emailカラムに'johndoe@example.com'を挿入しています。

### データの更新

データの更新には、以下のように記述します。

```php
DB::table('users')
    ->where('id', 1)
    ->update(['votes' => 1]);
```

上記の例では、usersテーブルのidが1のレコードのvotesカラムを1に更新しています。

### データの削除

データの削除には、以下のように記述します。

```php
DB::table('users')->where('votes', '<', 100)->delete();
```

上記の例では、usersテーブルのvotesカラムが100未満のレコードを削除しています。

## Eloquent ORMの基本

Eloquent ORMは、QueryBuilderよりも高度なオブジェクト指向的なデータベース操作が可能です。以下では、Eloquent ORMの基本的な使い方を解説します。

### モデルの作成

まずは、モデルの作成から始めます。以下のコマンドを実行すると、appディレクトリ内にUserモデルが作成されます。

```php
php artisan make:model User
```

### データの取得

データの取得には、以下のように記述します。

```php
$users = App\Models\User::all();
```

上記の例では、Userモデルに紐づくusersテーブルの全てのレコードを取得しています。allメソッド以外にも、findメソッドやwhereメソッドなど、取得方法は様々あります。詳細は公式ドキュメントを参照してください。

### データの挿入

データの挿入には、以下のように記述します。

```php
$user = new App\Models\User;
$user->name = 'John Doe';
$user->email = 'johndoe@example.com';
$user->save();
```

上記の例では、Userモデルを使って、nameカラムに'John Doe'、emailカラムに'johndoe@example.com'を挿入しています。

### データの更新

データの更新には、以下のように記述します。

```php
$user = App\Models\User::find(1);
$user->votes = 1;
$user->save();
```

上記の例では、Userモデルを使って、idが1のレコードのvotesカラムを1に更新しています。

### データの削除

データの削除には、以下のように記述します。

```php
$user = App\Models\User::find(1);
$user->delete();
```

上記の例では、Userモデルを使って、idが1のレコードを削除しています。

以上が、Laravelでのデータベース操作の基本とEloquent ORMの基本的な使い方です。次の章では、Eloquent ORMでよく使われる機能について解説します。

## Eloquent ORMの機能

### リレーション

Eloquent ORMでは、リレーションという機能を使って、複数のテーブルを結合してデータを取得することができます。

例えば、UserモデルとPostモデルがある場合、以下のようにリレーションを定義することができます。

```php
class User extends Model
{
    public function posts()
    {
        return $this->hasMany(Post::class);
    }
}
```

上記の例では、Userモデルにhasmanyメソッドを使って、Postモデルとのリレーションを定義しています。このように定義することで、以下のようにユーザーに紐づく投稿を取得することができます。

```php
$user = App\Models\User::find(1);
$posts = $user->posts;
```

### クエリスコープ

Eloquent ORMでは、クエリスコープという機能を使って、繰り返し使われるクエリを切り出して、再利用することができます。

例えば、Userモデルに、管理者権限を持つユーザーを取得するスコープを定義する場合、以下のように記述します。

```php
class User extends Model
{
    public function scopeAdmin($query)
    {
        return $query->where('admin', true);
    }
}
```

上記の例では、scopeメソッドを使って、adminメソッドを定義しています。このメソッドを使って、以下のように管理者ユーザーを取得することができます。

```php
$admins = App\Models\User::admin()->get();
```

### ミューテタ

Eloquent ORMでは、ミューテタという機能を使って、データを保存する前や取得する前に、自動的に加工することができます。

例えば、Userモデルに、名前を全て大文字にするミューテタを定義する場合、以下のように記述します。

```php
class User extends Model
{
    public function setNameAttribute($value)
    {
        $this->attributes['name'] = strtoupper($value);
    }
}
```

上記の例では、setNameAttributeメソッドを定義して、名前を全て大文字に変換しています。このメソッドを使って、以下のようにユーザーを作成することができます。

```php
$user = new App\Models\User;
$user->name = 'John Doe';
$user->email = 'johndoe@example.com';
$user->save();
```

上記の例では、ミューテタによって、自動的に名前が大文字に変換されています。

## まとめ

今回は、Laravelのデータベース操作の基本とEloquent ORMについて解説しました。データベース操作には、QueryBuilderとEloquent ORMの2つの方法があります。Eloquent ORMは、QueryBuilderよりも高度なオブジェク

　

## Laravel 関連のまとめ
https://hack-note.com/summary/laravel-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

