【Python】JSONを扱う方法
Python,JSON
python-use-json

こんにちは。今回は、Pythonについて初心者エンジニアに向けて、JSONを扱う方法をご紹介します。

## JSONとは

JSON(JavaScript Object Notation)は、データをクライアントとサーバーの間で簡単にやりとりするための形式です。JavaScriptで使用されるオブジェクトの記法を参考に、テキストベースの軽量な文書形式で記述されます。PythonでもJSONを扱うことができます。

## JSONの書式

JSONは、以下のような書式で表現されます。

```json
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

上記の例では、"name"という名前で"John"という値、"age"という名前で30という値、"city"という名前で"New York"という値がそれぞれ設定されています。

## PythonでJSONを扱う方法

Pythonでは、JSONを扱うための標準ライブラリが用意されています。JSON形式の文字列をPythonのデータ型に変換する方法と、Pythonのデータ型をJSON形式の文字列に変換する方法をそれぞれご紹介します。

### JSON形式の文字列をPythonのデータ型に変換する方法

JSON形式の文字列をPythonのデータ型に変換するには、json.loads()メソッドを使用します。以下は、JSON形式の文字列をPythonのデータ型に変換する例です。

```python
import json

# JSON形式の文字列
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# JSON形式の文字列をPythonのデータ型に変換する
data = json.loads(json_string)

# データ型を表示する
print(type(data)) # <class 'dict'>
print(data["name"]) # John
```

### Pythonのデータ型をJSON形式の文字列に変換する方法

Pythonのデータ型をJSON形式の文字列に変換するには、json.dumps()メソッドを使用します。以下は、Pythonのデータ型をJSON形式の文字列に変換する例です。

```python
import json

# Pythonのデータ型
data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Pythonのデータ型をJSON形式の文字列に変換する
json_string = json.dumps(data)

# JSON形式の文字列を表示する
print(json_string) # {"name": "John", "age": 30, "city": "New York"}
```

## まとめ

Pythonでは、JSONを扱うための標準ライブラリが用意されています。JSON形式の文字列をPythonのデータ型に変換するには、json.loads()メソッドを使用し、Pythonのデータ型をJSON形式の文字列に変換するには、json.dumps()メソッドを使用します。是非、JSONを扱う際にはこの方法を参考にしてみてください。

>本記事で使用するコードはサンプルであり、実際に利用する際には適切なチェックやバリデーションを行ってください。

参考にしたブログ記事:
- [PythonでJSONを扱う方法](https://www.atmarkit.co.jp/ait/articles/1910/04/news028.html)
- [PythonでJSONデータを取得する方法](https://qiita.com/Taiga__/items/5dcd4e5e5e9e5837b514)

## データサイエンティストスクール 無料部分あります
PythonやRなどのプログラミングを学ぶなら、
さらに統計分野を学習してデータサイエンティストを目指すのがおすすめ！

ディープラーニングやビックデータ分析などの高額システム案件の受注にも有利になります。

システム開発より、分析がやりたい方向けですが、下記載せておきます。

https://hack-note.com/programming-schools/#toc17

　

## Python 関連のまとめ
https://hack-note.com/summary/python-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
 
