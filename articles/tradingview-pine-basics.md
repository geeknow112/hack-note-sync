【tradingview】pineスクリプトの基礎知識と使い方解説
tradingview,pine
tradingview-pine-basics

## tradingview pine scriptについて初心者エンジニアに向けて

こんにちは。今回は、tradingview pine scriptについて初心者エンジニアに向けて、基礎知識と使い方を解説します。tradingviewは非常に人気のあるトレーディングプラットフォームであり、pine scriptはその独自のスクリプト言語です。pine scriptを使用することで、独自のカスタムインジケーターやトレードアラートなどを作成することができます。では、具体的にpineスクリプトの概要と基本的な構造から始めてみましょう。

## pineスクリプトの概要と基本構造

pineスクリプトは、トレーディングビューでのトレードアプリケーションを作成するための言語です。pineスクリプトは、チャート上にカスタムインジケーターやオシレーターを表示したり、トレードエントリーポイントやエグジットポイントを特定するために使用されます。

pineスクリプトは、以下のような基本的な構造を持っています。

```pine
//@version=4
study("myscript")

// 主要なロジックやインジケーターの計算
// ...

// チャートへの描画
plot(close)
```

このスクリプトでは、`study`関数を使用してインジケーターを作成し、`plot`関数を使用してその結果を描画しています。また、`//@version`タグを使用して使用するバージョンを指定することもできます。

## 変数とデータ型：pineスクリプトの基礎要素

pineスクリプトでは、変数を使用してデータを保存することができます。変数は、データ型に基づいて宣言されます。

```pine
//@version=4
study("myscript")

// 整数型の変数
var int myint = 10

// 浮動小数点数型の変数
var float myfloat = 10.5

// 真偽値型の変数
var bool mybool = true

// 文字列型の変数
var string mystring = "hello"

// 配列型の変数
var float[] myarray = array.new_float(2)
array.set(myarray, 0, 1.0)
array.set(myarray, 1, 2.0)

// デバッグ表示
plot(myint)
plot(myfloat)
plot(mybool)
plot(mystring)
plot(array.get(myarray, 0))
```

このスクリプトでは、それぞれのデータ型に対応した変数を宣言し、それらをプロットしています。配列型の変数にデータを追加するには、`array.new_float`関数を使用して配列を作成し、`array.set`関数を使用して要素を設定する必要があります。また、デバッグ表示には、`plot`関数を使用して変数をチャート上にプロットしています。

## 条件文と演算子：ロジックの組み立て方

pineスクリプトでは、条件文と演算子を使用して複雑なロジックを組み立てることができます。以下の例では、移動平均線が価格より上にある場合に買いエントリーを行うロジックを示しています。

```pine
//@version=4
study("myscript")

// 移動平均線
length = 10
ma = sma(close, length)

// 買いエントリー条件
buycondition = close > ma

// 買いエントリーのプロット
plotshape(buycondition, "buy", color.green, 0, style.labelup)
```

このスクリプトでは、`sma`関数を使用して移動平均線を計算し、`>`演算子を使用して価格が移動平均線よりも上にあるかどうかを判断しています。`plotshape`関数を使用して、買いエントリーの条件が満たされた場合にラベルをプロットしています。

## インジケーターと関数の使用方法

pineスクリプトでは、様々な組み込みのインジケーターや関数を使用することができます。以下は、rsi（relative strength index）インジケーターを使用した例です。

```pine
//@version=4
study("myscript")

// rsiインジケーター
length = 14
rsivalue = rsi(close, length)

// rsiのプロット
plot(rsivalue, "rsi", color.blue)
```

このスクリプトでは、`rsi`関数を使用してrsiを計算し、その結果をプロットしています。`plot`関数を使用して、計算したrsiをライングラフで表示しています。

## pineスクリプトのチャート描画とアノテーション機能

pineスクリプトでは、描画やアノテーション機能を使用してチャートに情報を表示することができます。以下の例では、移動平均線と買いエントリーポイントをチャートに表示します。

```pine
//@version=4
study("myscript")

// 移動平均線
length = 10
ma = sma(close, length)

// 移動平均線のプロット
plot(ma, color.blue)

// 買いエントリーポイントのチャート描画
buycondition = close > ma
plotshape(buycondition, "buy entry", color.green, 0, style.labelup)
```

このスクリプトでは、移動平均線を青色で、買いエントリーポイントを緑色のラベルとしてチャート上に表示しています。`plot`関数を使用して移動平均線を描画し、`plotshape`関数を使用して買いエントリーポイントをプロットしています。

以上が、tradingview pine scriptの基礎知識と使い方の解説でした。pineスクリプトを使用することで、独自のトレード戦略や指標を作成することができます。さらに詳しい情報や例を参考にするためには、公式ドキュメントやトレーディングビューブログなどを参照してください。

参考記事：
- [tradingviewの公式ドキュメント](https://www.tradingview.com/pine-script-docs/en/v4/)
- [tradingviewブログ記事「pine scriptによる10分で作る自作インジケーター入門」](https://jp.tradingview.com/blog/jpine%e5%88%a9%e7%94%a8%e8%80%85%e6%a7%98%e3%81%aepinescript%e3%82%b3%e3%83%bc%e3%83%89%e8%aa%ad%e8%a7%a3%e3%83%ac%e3%82%b7%e3%83%94-47264/)

　

## 【TradingView】Pine Script関連のまとめ
https://hack-note.com/summary/tradingview-pine-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

