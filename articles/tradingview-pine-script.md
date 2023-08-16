【Tradingview】Pine Script入門
tradingview,pine,テクニカル分析
tradingview-pine-script

こんにちは。今回は、Tradingviewについて初心者エンジニア向けて、Pine Scriptの基礎について解説します。

## はじめに

Tradingviewは、株式や仮想通貨などのチャート分析を行うためのツールです。Pine Scriptは、Tradingviewのために作られたプログラミング言語で、独自のテクニカル分析指標や自動売買システムを作ることができます。

本記事では、Pine Scriptの基礎を学び、サンプルコードを通じて実際に使い方を解説します。

## Pine Scriptとは

Pine Scriptは、Tradingviewのために作られたプログラミング言語で、チャート分析や自動売買システムの開発に利用されます。Pine Scriptの特徴は、シンプルな文法と高い拡張性です。

Pine Scriptは、Tradingviewのチャート上に表示されるテクニカル分析指標を作成するためにも利用されます。テクニカル分析指標とは、株式や仮想通貨などの価格や出来高などの統計的データから、未来の価格変動を予想するための指標のことです。

## Pine Scriptの基礎

### 変数と演算子

Pine Scriptでは、変数や演算子を用いて計算を行います。変数は、値を格納するために利用されます。以下は、変数の例です。

```python
//@version=5
study(title="My Script")
var x = 1
```

変数は、`var`キーワードを用いて宣言します。上記の例では、変数`x`に値`1`を格納しています。

演算子は、数値計算や論理演算などを行うために利用されます。以下は、演算子の例です。

```python
//@version=5
study(title="My Script")
var x = 1
var y = 2
var z = x + y
```

上記の例では、変数`z`に変数`x`と変数`y`を足した値を格納しています。

### 関数

Pine Scriptでは、関数を用いて複雑な計算を行うことができます。以下は、関数の例です。

```python
//@version=5
study(title="My Script")
f_my_function(x, y) => x + y
var z = f_my_function(1, 2)
```

上記の例では、関数`f_my_function`を定義して、変数`z`に関数を実行した結果を格納しています。

### プロット

Pine Scriptでは、`plot`関数を用いてチャート上にデータを表示することができます。以下は、プロットの例です。

```python
//@version=5
study(title="My Script")
plot(close)
```

上記の例では、`plot`関数を用いて、チャート上に`close`という変数を表示しています。

## サンプルコード

### 移動平均線

移動平均線は、株式や仮想通貨などの価格変動のトレンドを把握するために利用されます。以下は、移動平均線の計算方法を示したサンプルコードです。

```python
//@version=5
study(title="Moving Average", overlay=true)
len = input(20, minval=1)
src = input(close, title="Source")
out = sma(src, len)
plot(out, color=color.blue)
```

上記のコードでは、移動平均線を計算しています。`len`変数には、移動平均線の期間を設定しています。`src`変数には、移動平均線の計算に用いる価格情報を設定しています。`out`変数には、移動平均線の計算結果を格納しています。`plot`関数を用いて、移動平均線をチャート上に表示しています。

### RSI

RSIは、Relative Strength Indexの略で、株式や仮想通貨などの相場が過買いまたは過売り状態にあるかを判断するために利用されます。以下は、RSIの計算方法を示したサンプルコードです。

```python
//@version=5
study(title="Relative Strength Index", shorttitle="RSI", format=format.price, precision=2, resolution="")
len = input(14, minval=1, title="Length")
src = input(close, title="Source")
up = rma(max(change(src), 0), len)
down = rma(-min(change(src), 0), len)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))
plot(rsi, title="RSI", color=color.blue)
```

上記のコードでは、RSIを計算しています。`len`変数には、RSIの期間を設定しています。`src`変数には、計算に用いる価格情報を設定しています。`up`変数には、価格上昇幅の平均を、`down`変数には価格下落幅の平均を計算しています。`rsi`変数には、RSIの計算結果を格納しています。`plot`関数を用いて、RSIをチャート上に表示しています。

## 注意点

- Pine Scriptは、Tradingviewでしか利用できません。
- Pine Scriptで作成したテクニカル分析指標は、必ずしも正確な予測を行うわけではありません。適切な判断が必要です。
- Pine Scriptは、プログラミング言語であるため、実行する前に必ずコードを確認しましょう。

:::message alert
Pine Scriptは、プログラミング言語であるため、初心者には難しい場合もあります。基礎的なプログラミング知識を身につけた上で、利用することをおすすめします。
:::

## まとめ

本記事では、Tradingviewで利用されるPine Scriptの基礎について解説しました。変数や演算子、関数、プロットについて学び、移動平均線やRSIのサンプルコードを通じて、Pine Scriptの使い方を理解しました。

Pine Scriptは、プログラミング言語であり、初心者には難しい場合もあります。しかし、独自のテクニカル分析指標を作成したり、自動売買システムを開発したりすることができるため、ぜひ活用してみてください。

　

## 【TradingView】関連のまとめ
https://hack-note.com/summary/tradingview-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

