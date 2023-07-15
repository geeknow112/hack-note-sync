// ```php
$name = "John";
echo "My name is $name";
// ```


// ```php
$age = 20;
if ($age >= 20) {
  echo "成年です";
} else {
  echo "未成年です";
}
// ```


// ```php
Route::get('/hello', function () {
    return 'Hello, World!';
});
// ```


// ```php
namespace App\Http\Controllers;

use Illuminate\Http\Request;

class UserController extends Controller
{
    public function index()
    {
        // ユーザー一覧を取得する処理
    }

    public function show($id)
    {
        // 特定のユーザーを取得する処理
    }
}
// ```


// ```php
<!DOCTYPE html>
<html>
<head>
    <title>Blog</title>
</head>
<body>
    <h1>Blog</h1>

    <ul>
        @foreach ($posts as $post)
            <li>{{ $post->title }}</li>
        @endforeach
    </ul>
</body>
</html>
// ```


// ```html
<div id="app">
    <p>{{ message }}</p>
</div>

<script>
    var app = new Vue({
        el: '#app',
        data: {
            message: 'Hello, Vue.js!'
        }
    });
</script>
// ```


// ```html
<template>
    <div>
        <h1>{{ title }}</h1>
        <p>{{ content }}</p>
    </div>
</template>

<script>
    export default {
        props: {
            title: String,
            content: String
        }
    }
</script>
// ```
