【tradingview】pineスクリプト：時間枠とタイムゾーンの設定
tradingview,pine
tradingview-pine-timeframes-timezone

こんにちは。今回は、tradingview pine scriptについて初心者エンジニアに向けて、時間枠とタイムゾーンの設定について解説します。

## pineスクリプトでの時間枠の指定方法

pineスクリプトでは、チャートに表示される時間枠をカスタマイズすることができます。デフォルトでは、分足（1分、5分、15分など）、時間足（1時間、4時間など）、日足、週足、月足の中から選択することができます。

時間枠を指定するためには、`study()` 関数の引数に `resolution` を指定します。以下に、それぞれの時間枠の指定方法を示します。

- 1分足: `resolution = "1"`
- 5分足: `resolution = "5"`
- 15分足: `resolution = "15"`
- 1時間足: `resolution = "60"`
- 4時間足: `resolution = "240"`
- 日足: `resolution = "d"`
- 週足: `resolution = "w"`
- 月足: `resolution = "m"`

以下は、5分足のローソク足を表示する例です。

```
//@version=4
study("custom timeframe example", overlay=true)

res = "5" // 5分足
res_milliseconds = input(5*60*1000, title="設定したい時間枠を選択してください")

// ローソク足の描画
plotcandle(open, high , low, close, title="custom timeframe candle", color = close >= open ? color.green : color.red, wickcolor=color.green, upcolor=color.green, downcolor=color.red, transp=0, editable=false)

// 時間枠の設定
study("custom timeframe", overlay=true)
study(res, "custom timeframe", "custom timeframe", color=color.red, resolution=res_milliseconds)
```

このように、`resolution` 引数に指定すれば任意の時間枠でチャートを表示することができます。

参考url:
- [custom timeframes](https://www.tradingview.com/blog/en/custom-timeframes-240/)
- [choose between 9 different chart types for your style of trading](https://www.tradingview.com/stock-charts-basics/types-of-charts/)

## タイムゾーン設定の重要性と使い方

タイムゾーンの設定は、テクニカル分析や取引のタイミングを行う上で非常に重要です。pineスクリプトでは、デフォルトではutc（協定世界時）が使用されますが、各国ごとのローカルタイムに変更することも可能です。

タイムゾーンを設定するには、`timezone` 関数を使用します。以下は、東京のタイムゾーンに変更する例です。

```
//@version=4
study("timezone example", overlay=true)

// タイムゾーンの設定
timezone('asia/tokyo')

// ローカルタイムの表示
local_time = timestamp(time, time)
local_hour = hour(local_time)
local_minute = minute(local_time)
local_second = second(local_time)

label_text = "local time: " + tostring(local_hour) + ":" + tostring(local_minute) + ":" + tostring(local_second)

// ラベルの描画
label.new(x=bar_index, y=high, text=label_text, xloc=xloc.bar_time, color=color.yellow, textcolor=color.black, style=label.style_none)

```

この例では、`timezone` 関数を使用して東京のタイムゾーンに設定しています。その後、`timestamp` 関数を使用してローカルタイムを計算し、その結果をラベルとして表示しています。

参考url:
- [how to use tradingview's local timezone](https://www.tradingheroes.com/how-to-use-tradingviews-local-timezone/)
- [how to change the timezone on tradingview](https://help.cryptoquant.com/getting-started-with-tradingview/how-to-change-the-timezone-on-tradingview)

## ローカルタイムとutcの変換方法

pineスクリプトでは、ローカルタイムとutc（協定世界時）の相互変換を行うことも可能です。この機能を使用することで、異なるタイムゾーン間での取引のタイミングを調整することができます。

ローカルタイムをutcに変換するには、`time` 関数を使用します。以下は、東京のローカルタイムをutcに変換する例です。

```
//@version=4
study("local time to utc example", overlay=true)

// タイムゾーンの設定
timezone('asia/tokyo')

// ローカルタイムをutcに変換
utc_time = time + (timenow - time)

// utcの時間と分を取得
utc_hour = hour(utc_time)
utc_minute = minute(utc_time)

label_text = "utc time: " + tostring(utc_hour) + ":" + tostring(utc_minute)

// ラベルの描画
label.new(x=bar_index, y=high, text=label_text, xloc=xloc.bar_time, color=color.yellow, textcolor=color.black, style=label.style_none)
```

この例では、`timezone` 関数を使用して東京のタイムゾーンに設定し、その後、`time` 関数を使用してローカルタイムをutcに変換しています。変換結果は、`hour` 関数と `minute` 関数を使用して取得し、ラベルとして表示しています。

参考url:
- [converting time zones in tradingview | pine script tutorial](https://youtu.be/nzsvcyuywcm)
- [tradingview pine script: how to convert utc time to local time](https://www.tradingheroes.com/tradingview-pine-script-convert-utc-time-local-time/)

## 時間枠とタイムゾーンの相互関係の理解

時間枠とタイムゾーンは密接に関連しており、相互に影響しあうことがあります。例えば、特定の時間枠でローカルタイムを取得したい場合は、タイムゾーンの設定が必要です。また、異なるタイムゾーン間での取引を行う場合は、タイムゾーンの変換も必要です。

pineスクリプトでは、時間枠とタイムゾーンを独自に設定することができます。これにより、自分の取引スタイルや地域に合わせたチャート分析が可能となります。

タイムゾーンの設定は、`study()` 関数や `timestamp()` 関数、`timezone()` 関数を使用することで行えます。

## タイムゾーンに基づいた条件文の活用法

タイムゾーンを設定することで、特定の時間帯に条件を設定することも可能です。これにより、例えば取引のタイミングを限定するなど、細かな条件分岐を実装することができます。

以下に、タイムゾーンに基づいた条件文を活用した例を示します。

```
//@version=4
study("timezone-based conditional example", overlay=true)

// タイムゾーンの設定
timezone('asia/tokyo')

// 現在のローカルタイムを取得
local_time = timestamp(time, time)
local_hour = hour(local_time)

// 特定の時間帯の条件分岐
is_trading_time = local_hour >= 9 and local_hour < 15

// 条件に応じて表示するメッセージを設定
message = is_trading_time ? "trading time" : "non-trading time"

// ラベルの描画
label.new(x=bar_index, y=high, text=message, xloc=xloc.bar_time, color=color.yellow, textcolor=color.black, style=label.style_none)
```

この例では、東京のタイムゾーンを設定し、`is_trading_time` 変数を使用して現在のローカルタイムが特定の時間帯に該当するかどうかを判定しています。その結果に応じて、表示するメッセージを設定し、ラベルとして表示しています。

参考url:
- [tradingview pine script – how to use the session and security functions](https://www.tradingcode.net/tradingview/language/pine-script-manual/session-security-functions/)
- [tradingview pineスクリプトにおける異なる時間枠へのアクセス方法](https://www.tradingview.com/features/playground/accessing-different-timeframes)

以上が、「tradingview pine scriptについて初心者エンジニアに向けて、時間枠とタイムゾーンの設定」についての解説となります。pineスクリプトでは、時間枠の指定やタイムゾーンの設定を行うことで、より効果的なチャート分析や取引のタイミングを行うことができます。是非、上記のサンプルコードや参考urlを活用して、自分に合った設定を行ってみてください。

　

## 【TradingView】Pine Script関連のまとめ
https://hack-note.com/summary/tradingview-pine-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

