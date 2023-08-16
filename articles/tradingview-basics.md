【tradingview】基本機能と使い方の解説
tradingview,python,pine
tradingview-basics

## tradingviewについて初心者エンジニアに向けて

こんにちは。今回は、tradingviewについて初心者エンジニアに向けて、基本機能と使い方について解説していきます。tradingviewは、株や仮想通貨、外国為替など、さまざまな市場のチャート分析や取引を行うためのオンラインツールです。初めて使うエンジニアにとっては、操作方法や機能の使い方がわかりにくいこともあるかもしれませんが、この記事を通じて基本的な操作を学び、スムーズにtradingviewを使いこなせるようになりましょう。

※tradingviewの基本的な機能と使い方について解説していますが、本ブログ記事ではプログラミングに関する内容は含まれておりません。プログラミングにおけるtradingviewの使い方に興味がある方は、公式のpineスクリプトドキュメントを参照してください。

## チャートの表示とカスタマイズ

まずはじめに、tradingviewの基本的なチャートの表示とカスタマイズ方法について説明します。tradingviewでは、複数のティックのチャートを表示することができます。ティックとは、市場の取引単位のことを指し、例えば株式の場合は1株単位になります。

以下のサンプルコードは、tradingviewでティックチャートを表示する方法です。

```python
//@version=4
study("tick chart", shorttitle="tc", overlay=true)
tickchartperiod = input(title="tick chart period", type=input.integer, defval=1000)
price = close
plot(price, "tick chart", color=color.green)
```

このコードでは、`//@version=4`でバージョン指定し、`study`関数でスクリプトの開始を宣言しています。`tickchartperiod`変数には表示するティックの数を設定し、`input`関数を使ってユーザーが設定できるようにしています。また、`plot`関数を使ってチャートを描画しています。

さらに、チャートのカスタマイズも可能です。例えば、以下のようにチャートの背景色や線の色、軸のラベルを変更することができます。

```python
//@version=4
study("customize chart", shorttitle="cc", overlay=false)
bgcolor(color=color.black, transp=90)
plot(close, color=color.blue, linewidth=2)
xaxislabelcolor = input(title="x-axis label color", type=input.color, defval=color.white)
yaxislabelcolor = input(title="y-axis label color", type=input.color, defval=color.white)
xaxistitlecolor = input(title="x-axis title color", type=input.color, defval=color.white)
yaxistitlecolor = input(title="y-axis title color", type=input.color, defval=color.white)
xaxislabelscolor = input(title="x-axis labels color", type=input.color, defval=color.white)
yaxislabelscolor = input(title="y-axis labels color", type=input.color, defval=color.white)
xaxistitlelabel = input(title="x-axis title label", type=input.string, defval="date", group="x-axis")
yaxistitlelabel = input(title="y-axis title label", type=input.string, defval="price", group="y-axis")
xaxislabels = input(title="x-axis labels", type=input.string, defval="jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec", group="x-axis")
yaxislabels = input(title="y-axis labels", type=input.string, defval="0,10,20,30,40,50,60,70,80,90,100", group="y-axis")
xaxiscolor = input(title="x-axis color", type=input.color, defval=color.white, group="x-axis")
yaxiscolor = input(title="y-axis color", type=input.color, defval=color.white, group="y-axis")
hline(50)
axis(title=yaxistitlelabel, titlecolor=yaxistitlecolor, color=yaxiscolor, labels=yaxislabels, labelsstyle=xaxislabelscolor)
axis(2, title=xaxistitlelabel, titlecolor=xaxistitlecolor, color=xaxiscolor, labels=xaxislabels, labelsstyle=yaxislabelscolor)
```

このコードでは、`bgcolor`関数を使ってチャートの背景色を変更しています。また、`plot`関数を使って線の色や太さを変更しています。さらに、`input`関数と`group`引数を使って、各軸のラベルや色をユーザーが設定できるようにしています。

## テクニカルインジケーターの追加と設定

次に、tradingviewでテクニカルインジケーターを追加して設定する方法について説明します。テクニカルインジケーターとは、価格や出来高などの情報から計算されるチャート上での数値のことで、トレンドや転換点などを分析するために利用されます。

以下のサンプルコードは、tradingviewで移動平均線を表示する方法です。

```python
//@version=4
study("moving average", shorttitle="ma", overlay=true)
length = input(title="length", type=input.integer, defval=20)
source = input(title="source", type=input.source, defval=close)
ma = sma(source, length)
plot(ma, "moving average", color=color.red)
```

このコードでは、`study`関数でスクリプトの開始を宣言しています。`length`変数には移動平均線の期間を、`source`変数には取引データのソース（例えば終値など）を設定しています。また、`sma`関数を使って移動平均線を計算し、`plot`関数を使ってチャート上に描画しています。

さらに、テクニカルインジケーターの設定も可能です。例えば、以下のようにテクニカルインジケーターのパラメータをユーザーが設定できるようにしています。

```python
//@version=4
study("customize indicator", shorttitle="ci", overlay=true)
length = input(title="length", type=input.integer, defval=20, minval=1)
source = input(title="source", type=input.source, defval=close)
colorline = input(title="line color", type=input.color, defval=color.blue)
colorfill = input(title="fill color", type=input.color, defval=color.blue)
std = stdev(source, length)
plot(0, "zero line", color=color.gray, linewidth=1)
plot(2 * std, "upper band", color=colorline, linewidth=1)
plot(-2 * std, "lower band", color=colorline, linewidth=1)
fill(2 * std, -2 * std, color=colorfill, transp=90)
```

このコードでは、`input`関数を使ってパラメータを設定できるようにしています。例えば、`length`変数には期間、`source`変数にはソース、`colorline`変数には線の色、`colorfill`変数には塗りつぶしの色を設定しています。

## 時間枠と期間の変更方法

次に、tradingviewで表示するチャートの時間枠と期間を変更する方法について説明します。tradingviewでは、1分足や1時間足など、さまざまな時間軸のチャートを表示することができます。また、表示する期間も指定することができます。

以下のサンプルコードは、tradingviewで日足チャートを表示する方法です。

```python
//@version=4
study("daily chart", shorttitle="dc", overlay=true)
chartresolution = input(title="chart resolution", type=input.string, defval="d", options=["1", "3", "5", "15", "30", "60", "d", "w", "m"])
chartperiod = input(title="chart period", type=input.integer, defval=365)
price = close
chartid = security(syminfo.tickerid, chartresolution, close)
plot(chartid, "daily chart", color=color.green, linewidth=2)
```

このコードでは、`chartresolution`変数には表示するチャートの時間枠を設定し、`chartperiod`変数には表示する期間を設定しています。また、`security`関数を使って指定された時間軸のチャートデータを取得し、`plot`関数で描画しています。

さらに、時間枠や期間をユーザーが設定できるようにすることもできます。以下の例では、`input`関数を使って時間枠と期間を指定できるようにしています。

```python
//@version=4
study("customize chart", shorttitle="cc", overlay=true)
chartresolution = input(title="chart resolution", type=input.string, defval="d", options=["1", "3", "5", "15", "30", "60", "d", "w", "m"])
chartperiod = input(title="chart period", type=input.integer, defval=365)
price = close
chartid = security(syminfo.tickerid, chartresolution, close)
plot(chartid, "customize chart", color=color.green, linewidth=2)
```

このコードでは、`input`関数を使ってユーザーが時間枠と期間を指定できるようにしています。`options`引数には選択肢を指定することで、ドロップダウンメニューで選択できるようにすることができます。

## 注文ツールの使い方と注文の発行

続いて、tradingviewでの注文ツールの使い方と注文の発行方法について説明します。tradingviewでは、直感的に注文を出すことができるツールが提供されており、簡単に取引を行うことができます。

以下のサンプルコードは、tradingviewで注文を発行する方法です。

```python
//@version=4
strategy("order tool", overlay=true)
stoplossprice = input(title="stop loss price", type=input.float, defval=50.0)
takeprofitprice = input(title="take profit price", type=input.float, defval=150.0)
quantity = input(title="quantity", type=input.integer, defval=1)
stoplosscondition = low < stoplossprice
takeprofitcondition = high > takeprofitprice
strategy.entry("long", strategy.long, when=takeprofitcondition)
strategy.close("long", when=stoplosscondition)
```

このコードでは、`strategy`関数でストラテジーの開始を宣言しています。ユーザーが設定したストップロス価格とテイクプロフィット価格を使って、注文を発行するロジックを記述しています。例えば、`strategy.entry`関数を使って「long」という注文を発行し、`strategy.close`関数を使って指定した条件で注文をクローズしています。

さらに、以下のようにユーザーが注文のタイミングや条件を設定できるようにすることもできます。

```python
//@version=4
strategy("customize order tool", overlay=true)
stoplossprice = input(title="stop loss price", type=input.float, defval=50.0)
takeprofitprice = input(title="take profit price", type=input.float, defval=150.0)
quantity = input(title="quantity", type=input.integer, defval=1)
stoplosscondition = close < stoplossprice
takeprofitcondition = close > takeprofitprice
whencondition = input(title="when condition", type=input.integer, defval=1, options=["1", "2", "3"])
if whencondition == 1
    strategy.entry("long", strategy.long, when=takeprofitcondition)
else if whencondition == 2
    strategy.entry("short", strategy.short, when=stoplosscondition)
else if whencondition == 3
    strategy.entry("long", strategy.long, when=takeprofitcondition)
    strategy.entry("short", strategy.short, when=stoplosscondition)
strategy.close("long", when=stoplosscondition)
strategy.close("short", when=takeprofitcondition)
```

このコードでは、`input`関数を使ってユーザーが注文の条件やタイミングを設定できるようにしています。そして、`if`文を使って条件に応じて注文を発行しています。

　

## 【TradingView】関連のまとめ
https://hack-note.com/summary/tradingview-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

