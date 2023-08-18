【tradingview】チャート分析ツールの活用方法
tradingview,python,pine
tradingview-chart-analysis-tools

こんにちは。今回は、tradingviewについて初心者エンジニアに向けて、チャート分析ツールの活用方法について解説します。

## キャンドルスティックチャートの解読と使い方

キャンドルスティックチャートは、価格の変動を示すためのグラフでよく使われています。1つのキャンドルは、一定時間内の価格の始値（オープン）、終値（クローズ）、最高値（ハイ）、最安値（ロー）を表しています。

以下のサンプルコードは、pythonとpineスクリプトを使用してtradingviewからキャンドルスティックチャートを取得し、解読する方法を示しています。

```python
import ccxt
import pandas as pd

exchange = ccxt.exchange({
    'apikey': 'your_api_key',
    'secret': 'your_secret'
})

symbol = 'btc/usd'
timeframe = '1h'

data = exchange.fetch_ohlcv(symbol, timeframe)
df = pd.dataframe(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

print(df.head())
```

このコードでは、ccxtライブラリを使用して取引所から適切なシンボルと時間枠を指定してデータを取得し、pandasを使用してデータを整理しています。取得したデータは、キャンドルスティックチャートの各要素を含むdataframeとして表示されます。

## テクニカルインジケーターの活用と分析手法

テクニカルインジケーターは、価格の動きを分析するために使用されるツールです。一般的なテクニカルインジケーターには、移動平均線、rsi、macdなどがあります。

以下のサンプルコードは、pineスクリプトを使用してtradingviewのチャートにテクニカルインジケーターを表示する方法を示しています。

```
//@version=4
study(title="moving average", shorttitle="ma", overlay=true)
length = input(20, minval=1, title="length")
src = input(close, title="source")
ma = sma(src, length)
plot(ma, title="moving average", color=color.blue, linewidth=2)
```

このコードでは、チャート上に移動平均線を表示するためのpineスクリプトを定義しています。パラメーターとして長さ（期間）とデータのソース（デフォルトは終値）を指定することができます。このスクリプトをtradingviewのパインエディターに貼り付け、チャートに移動平均線を表示することができます。

## ボリンジャーバンドの使用と相場のボラティリティ分析

ボリンジャーバンドは、価格の変動範囲を示すために使用されるテクニカルインジケーターの1つです。ボリンジャーバンドは、中央移動平均線（sma）と上下の標準偏差ラインから構成されています。

以下のサンプルコードは、pythonとpineスクリプトを使用してtradingviewからボリンジャーバンドを計算し、相場のボラティリティを分析する方法を示しています。

```python
import ccxt
import pandas as pd
import numpy as np

exchange = ccxt.exchange({
    'apikey': 'your_api_key',
    'secret': 'your_secret'
})

symbol = 'btc/usd'
timeframe = '1h'

data = exchange.fetch_ohlcv(symbol, timeframe)
df = pd.dataframe(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

sma = df['close'].rolling(window=20).mean()
std = df['close'].rolling(window=20).std()
upper_band = sma + 2 * std
lower_band = sma - 2 * std

df['sma'] = sma
df['upper_band'] = upper_band
df['lower_band'] = lower_band

print(df.head())
```

このコードでは、ccxtライブラリを使用して取引所からデータを取得し、pandasを使用してボリンジャーバンドの各要素を計算しています。取得したデータには、中央移動平均線、上部バンド、下部バンドなどが含まれます。これにより、トレーダーは相場のボラティリティを分析することができます。

## 移動平均線の利用とトレンドの把握方法

移動平均線は、価格の平均値を一定期間で計算したものです。移動平均線は、短期の移動平均線と長期の移動平均線の組み合わせにより、トレンドの把握やサポート・レジスタンスレベルの特定などに使用されます。

以下のサンプルコードは、pineスクリプトを使用してtradingviewのチャートに移動平均線を表示する方法を示しています。

```
//@version=4
study(title="moving average crossover", shorttitle="ma crossover", overlay=true)
fast_length = input(9, minval=1, title="fast length")
slow_length = input(21, minval=1, title="slow length")
src = input(close, title="source")
fast_ma = sma(src, fast_length)
slow_ma = sma(src, slow_length)
plot(fast_ma, title="fast ma", color=color.blue, linewidth=2)
plot(slow_ma, title="slow ma", color=color.red, linewidth=2)
```

このコードでは、チャート上に短期の移動平均線と長期の移動平均線を表示するためのpineスクリプトを定義しています。パラメーターとして移動平均線の期間とデータのソース（デフォルトは終値）を指定することができます。このスクリプトをtradingviewのパインエディターに貼り付け、チャートに移動平均線を表示することができます。

## rsi（相対力指数）の解説と過買い・過売りの判断

rsi（相対力指数）は、価格の上昇圧力と下降圧力を示すために使用されるテクニカルインジケーターです。rsiは、0から100の範囲で表され、70以上は過買い状態、30以下は過売り状態とみなされます。

以下のサンプルコードは、pythonとpineスクリプトを使用してtradingviewからrsiを計算し、過買いと過売りの判断をする方法を示しています。

```python
import ccxt
import pandas as pd
import talib

exchange = ccxt.exchange({
    'apikey': 'your_api_key',
    'secret': 'your_secret'
})

symbol = 'btc/usd'
timeframe = '1h'

data = exchange.fetch_ohlcv(symbol, timeframe)
df = pd.dataframe(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

rsi = talib.rsi(df['close'], timeperiod=14)

df['rsi'] = rsi

print(df.head())
```

このコードでは、ccxtライブラリを使用して取引所からデータを取得し、talibライブラリを使用してrsiを計算しています。取得したデータには、rsiの値が含まれており、トレーダーは過買いと過売りの判断をすることができます。

## フィボナッチリトレースメントの活用とサポート・レジスタンスの設定

フィボナッチリトレースメントは、価格のトレンドの押し戻し水準やサポート・レジスタンスレベルを見つけるために使用されるツールです。フィボナッチリトレースメントは、トレンドの高値と安値の間に水平なライン（フィボナッチライン）を描くことで構成されています。

以下のサンプルコードは、pineスクリプトを使用してtradingviewのチャートにフィボナッチリトレースメントを表示する方法を示しています。

```
//@version=4
study(title="fibonacci retracement", shorttitle="fib retracement", overlay=true)
high_price = input(100, title="high price")
low_price = input(50, title="low price")
level_1 = input(0.382, title="level 1", step=0.01)
level_2 = input(0.618, title="level 2", step=0.01)
plot(high_price, title="high", color=color.green, linewidth=2)
plot(low_price, title="low", color=color.red, linewidth=2)
plot(high_price - (high_price - low_price) * level_1, title="level 1", color=color.orange, linewidth=1)
plot(high_price - (high_price - low_price) * level_2, title="level 2", color=color.blue, linewidth=1)
```

このコードでは、チャート上にトレンドの高値と安値を指定し、フィボナッチリトレースメントの水平なラインを表示するためのpineスクリプトを定義しています。パラメーターとして高値、安値、および各フィボナッチレベルを指定することができます。このスクリプトをtradingviewのパインエディターに貼り付け、チャートにフィボナッチリトレースメントを表示することができます。

以上が、tradingviewのチャート分析ツールの活用方法についての解説です。初心者エンジニアの方に役立つ情報を提供できたら幸いです。参考になるブログ記事として、下記のリンクをご覧ください。

- [tradingview公式ブログ](https://www.tradingview.com/blog/)
- [tradingviewの使い方ガイド](https://note.com/kabukurinote/n/nf5e5d3c8b3d8)

　

## 【TradingView】関連のまとめ
https://hack-note.com/summary/tradingview-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

