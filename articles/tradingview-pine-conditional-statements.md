【tradingview】pineスクリプト：条件文と制御フロー
tradingview,pine
tradingview-pine-conditional-statements

## tradingview pine scriptについて初心者エンジニアに向けて

こんにちは。今回は、tradingview pine scriptについて初心者エンジニア向けに解説していきます。tradingviewは、主に株式や仮想通貨などのチャート分析を行うためのプラットフォームです。そして、pine scriptは、tradingview上で使用できる独自のスクリプト言語です。

pine scriptを使うことで、自動売買システムやテクニカルインジケータなどを作成することができます。その中でも条件文と制御フローの理解は非常に重要です。条件文を使うことで、ある条件が満たされた場合に特定の処理を実行することができます。制御フローは、条件分岐やループ処理などのフロー制御を行うための機能です。

それでは、具体的なコードを交えながら、各機能について詳しく解説していきましょう。

## if文の使用と条件式の書き方

if文は、最も基本的な条件分岐の手法です。ある条件が真である場合に特定の処理を実行し、偽である場合には別の処理を実行することができます。

```pinescript
//@version=4
study("if文の使用例", shorttitle="if example")

length = input(14, minval=1, title="length")
ma = sma(close, length)
price = close

if price > ma
    strategy.entry("long", strategy.long)
    plotshape(price, title="buy arrow", shape=shape.triangleup, color=color.green, style=shape.style_labelup)
else
    strategy.entry("short", strategy.short)
    plotshape(price, title="sell arrow", shape=shape.triangledown, color=color.red, style=shape.style_labeldown)
```

上記のコードでは、現在の価格が移動平均よりも高ければ買いエントリーを行い、逆に低ければ売りエントリーを行うという処理が行われます。また、価格をプロットし、買いシグナルでは緑の三角形、売りシグナルでは赤の三角形がチャート上に表示されます。

## 複数の条件を組み合わせる方法

多くの場合、複数の条件を組み合わせる必要があります。このときには、論理演算子を使用して条件を組み合わせることができます。論理演算子には、and(```and```), or(```or```), not(```not```)の3つがあります。

```pinescript
//@version=4
study("複数の条件を組み合わせる例", shorttitle="multiple conditions")

length = input(14, minval=1, title="length")
ma = sma(close, length)
price = close

if price > ma and volume > 100000
    strategy.entry("long", strategy.long)
    plotshape(price, title="buy arrow", shape=shape.triangleup, color=color.green, style=shape.style_labelup)
else
    strategy.entry("short", strategy.short)
    plotshape(price, title="sell arrow", shape=shape.triangledown, color=color.red, style=shape.style_labeldown)
```

上記の例では、現在の価格が移動平均よりも高く、かつ出来高が10万株以上である場合にのみ買いエントリーを行うという条件を設定しています。このように、複数の条件を組み合わせることで、より柔軟なトレード戦略を実現することができます。

## else文とelseif文の活用法

条件式が真でない場合に実行される処理を設定するためには、else文を使用します。elseif文を使用することで、複数の条件を順に判定し、最初に真となった条件の処理のみを実行することができます。

```pinescript
//@version=4
study("else文とelseif文の使用例", shorttitle="else and elseif example")

length = input(14, minval=1, title="length")
ma = sma(close, length)
price = close

if price > ma
    strategy.entry("long", strategy.long)
    plotshape(price, title="buy arrow", shape=shape.triangleup, color=color.green, style=shape.style_labelup)
else if price < ma
    strategy.entry("short", strategy.short)
    plotshape(price, title="sell arrow", shape=shape.triangledown, color=color.red, style=shape.style_labeldown)
else
    plotshape(price, title="no entry", shape=shape.labelup, location=location.belowbar, color=color.yellow, text="no entry")
```

上記の例では、現在の価格が移動平均よりも高い場合には買いエントリーを、逆に低い場合には売りエントリーを行います。それ以外の場合にはエントリーを行わないことを示すメッセージがチャート上に表示されます。

## forループと配列の要素処理

forループは、ある処理を指定した回数繰り返すためのループ構造です。配列を使うことで、複数の要素を持つデータを効率的に処理することができます。

```pinescript
//@version=4
study("forループと配列の使用例", shorttitle="for loop and array example")

symbols = ["btc", "eth", "xrp", "bch", "ltc"]
length = input(14, minval=1, title="length")

for s in symbols
    ma = sma(close, length, title="sma")
    plot(ma, title=s + "sma", color=color.blue)
```

上記の例では、5つの仮想通貨のsma(simple moving average)を計算し、チャート上にプロットしています。forループを使用することで、繰り返し処理を行いながら各仮想通貨ごとにsmaを計算することができます。

## breakとcontinueの制御フロー

break文は、ループから抜け出すための制御フローです。continue文は、ループの次の繰り返しにジャンプするための制御フローです。

```pinescript
//@version=4
study("breakとcontinueの使用例", shorttitle="break and continue example")

length = input(14, minval=1, title="length")
ma = sma(close, length, title="sma")

for i = 1 to 20
    if i % 3 == 0
        continue
    plot(ma * i, title="plot " + str.tostring(i), color=color.blue)

    if i > 10
        break
```

上記の例では、1から20までの整数に対して以下の処理を行います。まず、3で割り切れる数の場合はcontinue文により次の繰り返しに進みます。それ以外の場合にはmaをi倍した値をプロットします。また、iが10を超えるとループを抜けます。

以上、tradingview pine scriptの条件文と制御フローについての解説でした。これらの機能を上手に活用することで、より複雑なトレードロジックを構築することができます。是非、自分自身のトレード戦略に応じてpine scriptを使いこなしてください。

　

## 【TradingView】Pine Script関連のまとめ
https://hack-note.com/summary/tradingview-pine-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

