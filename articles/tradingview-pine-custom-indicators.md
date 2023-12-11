【tradingview】pineスクリプトのカスタムインジケーター作成入門
tradingview,pine
tradingview-pine-custom-indicators

## tradingview pine scriptについて初心者エンジニアに向けて

こんにちは。今回は、tradingview pine scriptについて初心者エンジニアに向けて、カスタムインジケーターの作成入門をご紹介します。tradingviewは、株式や仮想通貨などの市場データをグラフィカルに表示し、テクニカル分析をサポートしてくれるツールです。pine scriptは、そのtradingview上で使用するためのプログラミング言語であり、自分自身のカスタムインジケーターやストラテジーを作成することができます。

pineスクリプトは、c言語に似た構文を持つ言語であり、パワフルな技術分析ツールを作成するために使用されます。この記事では、pineスクリプトの基礎から始めて、データ操作、算術演算子、プロット、条件分岐とループ、最適化とパフォーマンス向上のテクニックなど、カスタムインジケーターの作成に必要な要素を紹介します。もしtradingviewで独自のインジケーターやストラテジーを使いたいと考えている初心者のエンジニアの方は、ぜひ参考にしてみてください。

## インジケーターの基本構造とpineスクリプトの基礎

まずは、pineスクリプトの基本的な構造について見ていきましょう。

```pinescript
//@version=4
study("custom indicator", overlay=true)

// 変数の宣言
var int variable = 0

// インジケーターの計算
if close > open
    variable := variable + 1
else if close < open
    variable := variable - 1
else
    variable := variable

// プロット
plot(variable, title="custom indicator", color=color.blue)
```

この例では、カスタムインジケーターの基本的な構造を示しています。まず、`//@version=4`という行は、pineスクリプトのバージョンを指定するものです。次に、`study()`関数により、tradingview上でカスタムインジケーターとして表示することを宣言しています。`overlay=true`というオプションは、インジケーターをチャートのメイングラフの上に重ねて表示することを指定しています。

その後、必要な変数を宣言し、インジケーターの計算を行います。この例では、`close > open`という条件で、`variable`という変数を操作しています。最後に、`plot()`関数でインジケーターの結果をチャート上にプロットしています。

## pineスクリプトのデータ操作と算術演算子の活用方法

pineスクリプトでは、市場データや計算結果などのデータを操作するための様々な関数と算術演算子が用意されています。ここでは、pineスクリプトでよく利用されるデータ操作と算術演算子の活用方法を紹介します。

```pinescript
//@version=4
study("data manipulation", overlay=true)

// 単純移動平均 (sma)
smavalue = sma(close, 10)

// 指数移動平均 (ema)
emavalue = ema(close, 10)

// データの加算
addvalue = close + open

// データの減算
subvalue = close - open

// データの乗算
mulvalue = close * open

// データの除算
divvalue = close / open

// データの剰余
modvalue = close % open

// データのべき乗
powvalue = pow(close, 2)

// データの平方根
sqrtvalue = sqrt(close)
```

この例では、代表的なデータ操作と算術演算子を使った計算を紹介しています。まず、`sma()`関数を使って、単純移動平均(sma)を計算しています。次に、`ema()`関数を使って、指数移動平均(ema)を計算しています。

その他の算術演算子としては、加算 `+`、減算 `-`、乗算 `*`、除算 `/`、剰余 `%`、べき乗 `pow()`、平方根 `sqrt()`などがあります。これらの演算子や関数を組み合わせて、複雑な計算を行うことができます。

## プロットとカラーリング：チャート上での情報表示と見やすさの向上

pineスクリプトでは、プロットとカラーリングを使って、インジケーターの計算結果やその他の情報をチャート上に表示することができます。以下に、その方法を紹介します。

```pinescript
//@version=4
study("plotting and coloring", overlay=true)

// プロット
plot(close, title="close", color=color.blue)

// ラインプロット
hline(50, title="middle line", color=color.gray)

// 背景カラーリング
bgcolor(close > open ? color.green : color.red, transp=70)
```

この例では、`plot()`関数を使って終値をプロットしています。`title`オプションを使うことで、プロットされるデータにタイトルを付けることができます。また、`hline()`関数を使って水平線をプロットしています。同様に、`vline()`関数を使って垂直線をプロットすることもできます。

さらに、`bgcolor()`関数を使って背景カラーリングを行っています。この関数では、条件に基づいてカラーを変えることができます。この例では、終値が始値よりも高ければ緑色、低ければ赤色の背景カラーを設定しています。

## 条件分岐とループ：トレードシグナルの生成と複雑な戦略の実装

pineスクリプトでは、条件分岐とループを使って、トレードシグナルの生成や複雑な戦略の実装を行うことができます。以下に、その方法を紹介します。

```pinescript
//@version=4
study("conditional statements and loops", overlay=true)

// 条件分岐
if close > open
    strategy.entry("buy", strategy.long)
else if close < open
    strategy.entry("sell", strategy.short)

// ループ
for i = 1 to 10
    strategy.close("buy", when=i == 5)
```

この例では、`if`文を使って条件分岐を行っています。ここでは終値と始値を比較し、終値が始値よりも高ければ`strategy.entry()`関数で買いシグナルを生成し、低ければ売りシグナルを生成しています。

また、`for`ループを使って特定の条件を満たすまでトレードポジションをクローズすることもできます。この例では、`strategy.close()`関数を使って、`"buy"`という名前のポジションを、`when`条件に基づいてクローズしています。

## インジケーターの最適化とパフォーマンス向上のためのテクニック

最後に、インジケーターの最適化とパフォーマンス向上のためのテクニックを紹介します。pineスクリプトでは、特定の期間や条件に基づいて計算やプロットを行い、パフォーマンスを向上させることができます。

```pinescript
//@version=4
study("optimization and performance", overlay=true)

// 最適化
totalcount = input(5, "total count")
smavalue = sma(close, 10)
plot(smavalue, title="sma", color=color.blue)

// 指定期間での計算
calcperiod = input("month", "calculation period", options=["day", "week", "month"])
periodclose = security(syminfo.tickerid, calcperiod, close)
plot(periodclose, title="period close", color=color.red, linewidth=2)
```

この例では、`input()`関数を使って最適化のパラメータや計算期間を指定することができます。`totalcount`という変数は、最適化するパラメータの初期値を指定するための入力欄を表示します。

また、`security()`関数を使って指定期間のデータを取得しています。`syminfo.tickerid`は、現在のティッカーのidを取得するために使用されます。これにより、異なるティッカーのデータを参照することができます。

以上が、tradingview pine scriptの基礎から応用までのカスタムインジケーター作成の入門ガイドでした。pineスクリプトの基本構造、データ操作と算術演算子の活用方法、プロットとカラーリング、条件分岐とループ、最適化とパフォーマンス向上のテクニックなど、様々な要素を覚えておくと、より自分自身のトレードシステムやインジケーターを作成する上で役立つことでしょう。ぜひ、実際にpineスクリプトを使って、自分自身のカスタムインジケーターを作成してみてください。

参考文献：
- [tradingview docs - introduction to pine script](https://www.tradingview.com/pine-script-docs/en/v4/index.html)
- [pine script tutorial - tradingview wiki](https://www.tradingview.com/wiki/pine_script_tutorial)

　

## 【TradingView】Pine Script関連のまとめ
https://hack-note.com/summary/tradingview-pine-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

