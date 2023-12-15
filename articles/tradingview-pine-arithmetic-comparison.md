【tradingview】pineスクリプト：算術演算子と比較演算子
tradingview,pine
tradingview-pine-arithmetic-comparison

## tradingview pine scriptについて初心者エンジニアに向けて

こんにちは。今回は、tradingviewのpineスクリプトについて初心者エンジニアに向けて、算術演算子と比較演算子について解説します。

pineスクリプトは、tradingviewで使われる独自のスクリプト言語であり、テクニカル分析やインジケータの作成に利用されます。初めてpineスクリプトに触れるエンジニアの方々もいらっしゃるかと思いますので、基本的な算術演算子と比較演算子の使い方について解説します。

### 算術演算子の基本的な使い方

算術演算子は、数値の四則演算を行うために使用されます。pineスクリプトで使用できる算術演算子は以下の通りです。

- 加算(+)：2つの数値を足し合わせる
- 減算(-)：2つの数値を引き算する
- 乗算(*)：2つの数値を掛け合わせる
- 除算(/)：2つの数値を割り算する
- 剰余(%)：2つの数値の除算の余りを求める（整数の割り算で使われる）

以下に、算術演算子の基本的な使い方のサンプルコードを示します。

```pine
//@version=5
study("算術演算子の基本的な使い方", overlay=true)

a = 10 + 5
b = 10 - 5
c = 10 * 5
d = 10 / 5
e = 10 % 7

plot(a, color=color.blue)
plot(b, color=color.red)
plot(c, color=color.green)
plot(d, color=color.orange)
plot(e, color=color.purple)
```

上記のコードでは、数値の加算・減算・乗算・除算・剰余をそれぞれ行い、結果をプロットしています。プロット結果は、それぞれ色分けされて表示されます。

### 数値の加算と減算のテクニック

次に、数値の加算と減算のテクニックについて解説します。pineスクリプトでは、数値の加算や減算に加えて、以下のようなテクニックも利用することができます。

- 前回の値からの差分を加算または減算する
- 前回の値を参照して、特定の条件が満たされた場合に加算または減算する

以下に、数値の加算と減算のテクニックのサンプルコードを示します。

```pine
//@version=5
study("数値の加算と減算のテクニック", overlay=true)

// 前回の値からの差分を加算または減算する
diff = 10
a = close + diff

// 前回の値を参照して、特定の条件が満たされた場合に加算または減算する
b = if(close > high[1])
    close + 5
else if(close < low[1])
    close - 5
else
    close

plot(a, color=color.blue)
plot(b, color=color.red)
```

上記のコードでは、加算と減算のテクニックを2つ紹介しています。`diff`という変数に数値を代入し、その値を`close`（現在の終値）に加算することで、前回の値からの差分を加算しています。また、`close`と前回の`high`（前回の高値）や`low`（前回の安値）を比較して、特定の条件が満たされた場合に加算または減算する方法も紹介しています。

### 乗算と除算の応用方法

次に、乗算と除算の応用方法について解説します。これらの演算子を使用することで、データの変換や加重平均の計算などを行うことができます。

以下に、乗算と除算の応用方法のサンプルコードを示します。

```pine
//@version=5
study("乗算と除算の応用方法", overlay=true)

// データの変換
a = close * 100 // 終値を100倍する
b = close / 100 // 終値を100分の1にする

// 加重平均の計算
weights = [0.1, 0.2, 0.3, 0.4]
c = close * weights[0] + close[1] * weights[1] + close[2] * weights[2] + close[3] * weights[3]

plot(a, color=color.blue)
plot(b, color=color.red)
plot(c, color=color.green)
```

上記のコードでは、乗算と除算の応用方法を2つ紹介しています。`a`と`b`では、終値`close`を100倍したり100分の1にしたりしてデータの変換を行っています。また、`c`では加重平均を計算しています。`weights`という配列に重みを設定し、終値`close`と重みを乗算して足し合わせることで、加重平均を求めることができます。

### 比較演算子の意味と使い方

続いて、比較演算子の意味と使い方について解説します。比較演算子は、2つの値の関係性を判定するために使用されます。

以下に、比較演算子の意味と使い方のサンプルコードを示します。

```pine
//@version=5
study("比較演算子の意味と使い方", overlay=true)

a = close > open // 終値が始値よりも大きい場合にtrue（1）を返す
b = close >= open // 終値が始値以上の場合にtrue（1）を返す
c = close < open // 終値が始値よりも小さい場合にtrue（1）を返す
d = close <= open // 終値が始値以下の場合にtrue（1）を返す
e = close == open // 終値と始値が等しい場合にtrue（1）を返す
f = close != open // 終値と始値が等しくない場合にtrue（1）を返す

plot(a, color=color.blue)
plot(b, color=color.red)
plot(c, color=color.green)
plot(d, color=color.orange)
plot(e, color=color.purple)
plot(f, color=color.gray)
```

上記のコードでは、比較演算子の意味と使い方を紹介しています。終値`close`と始値`open`の関係性を判定し、その結果をプロットしています。たとえば、`a`では終値が始値よりも大きい場合にtrue（1）を返し、`f`では終値と始値が等しくない場合にtrue（1）を返します。

### 複数の条件を組み合わせる方法

最後に、複数の条件を組み合わせる方法について解説します。pineスクリプトでは、複数の条件を組み合わせるために論理演算子が使用されます。論理演算子には、以下の3つがあります。

- and（&&）：2つの条件が同時に成り立つ場合にtrue（1）を返す
- or（||）：2つの条件のうち、少なくとも1つが成り立つ場合にtrue（1）を返す
- not（!）：条件の否定を行い、true（1）とfalse（0）を反転させる

以下に、複数の条件を組み合わせる方法のサンプルコードを示します。

```pine
//@version=5
study("複数の条件を組み合わせる方法", overlay=true)

a = close > open && high > low // 終値が始値よりも大きく、高値が安値よりも大きい場合にtrue（1）を返す
b = close > open || high > low // 終値が始値よりも大きいか、または高値が安値よりも大きい場合にtrue（1）を返す
c = !(close == open) // 終値と始値が等しくない場合にtrue（1）を返す

plot(a ? 1 : 0, color=color.blue)
plot(b ? 1 : 0, color=color.red)
plot(c ? 1 : 0, color=color.green)
```

上記のコードでは、複数の条件を組み合わせる方法を紹介しています。`a`では終値が始値よりも大きく、かつ高値が安値よりも大きい場合にtrue（1）を返し、`b`では終値が始値よりも大きいか、または高値が安値よりも大きい場合にtrue（1）を返します。`c`では終値と始値が等しくない場合にtrue（1）を返します。プロット結果は、条件が成り立つ場合に1を返し、成り立たない場合に0を返します。

### まとめ

tradingviewのpineスクリプトの算術演算子と比較演算子について解説しました。算術演算子を使用することで数値の四則演算を行い、乗算や除算を利用することでデータの変換や加重平均の計算が可能となります。比較演算子を使用することで、複数の条件を組み合わせることや関係性を判定することができます。

pineスクリプトの算術演算子と比較演算子を駆使して、さまざまなテクニカル分析やインジケータの作成を行ってみてください。

## 参考記事

- [pine script language tutorial](https://www.tradingview.com/pine-script-docs/ja/v5/tutorial/)
- [the definitive guide to tradingview programming](https://zenandtheartoftrading.com/tradingview-programming)

以上で、tradingview pine scriptの算術演算子と比較演算子の使い方についての解説を終わります。初心者の方にとっても理解しやすいように説明しましたので、ぜひ参考にしてください。より高度な応用については、公式ドキュメントや参考記事をご覧いただきながら、pineスクリプトの習得を進めていってください。

　

## 【TradingView】Pine Script関連のまとめ
https://hack-note.com/summary/tradingview-pine-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

