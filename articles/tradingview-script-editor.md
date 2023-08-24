【tradingview】スクリプトエディターの使い方と自動売買戦略の作成
tradingview,python,pine
tradingview-script-editor

## tradingviewについて初心者エンジニアに向けて、スクリプトエディターの使い方と自動売買戦略の作成を解説

こんにちは。今回は初心者エンジニアの方に向けて、tradingviewについて解説していきます。具体的には、tradingviewのスクリプトエディターの使い方や自動売買戦略の作成方法について詳しく説明していきます。tradingviewは、株式、仮想通貨、外国為替などの様々な市場でチャートの分析を行うためのツールで、初心者エンジニアの方にとっても非常に役立つものとなっています。

tradingviewのスクリプトエディターは、pineという言語を使用して自動売買戦略を作成するためのものです。pineは、tradingview独自のスクリプト言語であり、pythonとは異なる構文やルールがあります。pineを使って自分だけのオリジナルの自動売買戦略を作成することができます。では、早速tradingviewのスクリプトエディターの使い方と自動売買戦略の作成方法を見ていきましょう。

## バックテストの基本と使い方の解説

バックテストとは、過去のデータを使って手法や戦略の検証を行うことです。tradingviewでは、スクリプトエディターを使用してバックテストを行うことができます。バックテストの基本的な使い方を解説します。

まず、スクリプトエディターを開きます。また、バックテストの設定を行います。設定項目には、テスト期間、テスト対象の銘柄、使用するテクニカル指標などがあります。次に、バックテストを実行し、結果を確認します。グラフ上にエントリーポイントやエグジットポイントが表示され、取引シミュレーションが行われます。バックテスト結果を分析し、改善点を特定することで、より良いパフォーマンスを得ることができます。

以下にバックテストのサンプルコードを示します。

```pine
//@version=4
strategy("my strategy", overlay=true)

longcondition = crossover(sma(close, 14), sma(close, 28))
shortcondition = crossunder(sma(close, 14), sma(close, 28))

strategy.entry("long", strategy.long, when=longcondition)
strategy.entry("short", strategy.short, when=shortcondition)

strategy.exit("exit", "long", "short")
```

このサンプルコードは、単純な移動平均線のクロスオーバーシグナルを使ったロングとショートのエントリーとエグジットを行う戦略です。まず、14期間の単純移動平均線と28期間の単純移動平均線のクロスオーバーを条件として設定しています。また、strategy.entry関数を使ってエントリーを、strategy.exit関数を使ってエグジットを行っています。

## バックテストのパフォーマンス評価指標の活用方法

バックテストにおいては、パフォーマンス評価指標を活用することで、戦略の評価や改善点の特定に役立ちます。tradingviewでは、様々なパフォーマンス評価指標を利用することができます。パフォーマンス評価指標の活用方法を解説します。

まず、スクリプトエディターのバックテスト結果画面に表示されているパフォーマンス情報を確認します。この情報には、収益率、勝率、最大損失、最大利益などが含まれています。これらの指標を分析することで、戦略の優劣を判断することができます。

さらに、パフォーマンス評価指標をグラフ化することも可能です。tradingviewのスクリプトエディターでは、パフォーマンスを可視化するための関数やプロット機能を提供しています。これにより、収益曲線やリターンドローダウン曲線などを描画することができます。

以下にパフォーマンス評価指標のグラフ化のサンプルコードを示します。

```pine
//@version=4
strategy("my strategy", overlay=true)

longcondition = crossover(sma(close, 14), sma(close, 28))
shortcondition = crossunder(sma(close, 14), sma(close, 28))

strategy.entry("long", strategy.long, when=longcondition)
strategy.entry("short", strategy.short, when=shortcondition)

strategy.exit("exit", "long", "short")

// パフォーマンス評価指標の可視化
strategy.equity("my strategy equity", overlay=true)
plot(strategy.equity)
```

このサンプルコードでは、strategy.equity関数を使ってエクイティ情報を可視化しています。エクイティグラフは、戦略の収益推移を表示するためのものであり、パフォーマンス評価指標の可視化に役立ちます。

## バックテストの設定とテスト期間の選び方

バックテストを行う際には、正しい設定とテスト期間の選択が重要です。tradingviewのスクリプトエディターでは、バックテストの設定とテスト期間を選ぶことができます。設定とテスト期間の選び方について解説します。

まず、設定項目の中で重要なのは、テスト対象の銘柄とテスト期間です。テスト対象の銘柄は、バックテストを行いたい銘柄を選択します。テスト期間は、バックテストを行う期間を選択します。通常、テスト期間は過去のデータを使用するため、適切な期間を選ぶことが重要です。

テスト期間の選び方には、過去のデータを分割して複数の期間でテストする方法や、連続した期間でテストする方法などがあります。また、テスト期間を変更することで、過去の相場の変動性やトレンドのパターンをテストすることができます。

以下にテスト期間の選び方のサンプルコードを示します。

```pine
//@version=4
strategy("my strategy", overlay=true)

longcondition = crossover(sma(close, 14), sma(close, 28))
shortcondition = crossunder(sma(close, 14), sma(close, 28))

strategy.entry("long", strategy.long, when=longcondition)
strategy.entry("short", strategy.short, when=shortcondition)

strategy.exit("exit", "long", "short")

// バックテストの設定
strategy("my strategy", overlay=true, initial_capital=10000, currency=currency.usd)

// テスト期間の選択
strategy("my strategy", overlay=true, from=timestamp("1 jan 2019 00:00"), to=timestamp("31 dec 2019 23:59"))
```

このサンプルコードでは、strategy関数の引数にテスト期間の設定が含まれています。fromとtoには、テスト期間を表すタイムスタンプを指定することができます。

## バックテスト結果の分析と改善点の特定

バックテストの結果を分析し、改善点を特定することは、戦略のパフォーマンスを向上させるために重要です。tradingviewのスクリプトエディターでは、バックテスト結果を詳細に分析することができます。バックテスト結果の分析と改善点の特定方法を解説します。

まず、バックテスト結果画面に表示されているパフォーマンス情報を詳細に確認します。収益率、勝率、最大損失、最大利益などの指標を分析し、戦略の優れた点や改善が必要な点を特定します。また、グラフやチャート上のエントリーポイントやエグジットポイントを分析し、戦略のエントリーやエグジットのタイミングを見直すことも重要です。

さらに、バックテスト結果を他の戦略や他のテスト期間と比較することも有効です。tradingviewのスクリプトエディターでは、複数の戦略やテスト期間を同時にバックテストすることができます。これにより、異なる戦略や期間での比較を行い、より良い戦略を見つけることができます。

以下にバックテスト結果の分析と改善点の特定のサンプルコードを示します。

```pine
//@version=4
strategy("my strategy", overlay=true)

longcondition = crossover(sma(close, 14), sma(close, 28))
shortcondition = crossunder(sma(close, 14), sma(close, 28))

strategy.entry("long", strategy.long, when=longcondition)
strategy.entry("short", strategy.short, when=shortcondition)

strategy.exit("exit", "long", "short")

// バックテスト結果の分析
strategy.equity("my strategy equity", overlay=true)
plot(strategy.equity)
```

このサンプルコードでは、バックテスト結果をエクイティグラフとして可視化しています。エクイティグラフは、戦略の収益推移を表示するためのものであり、分析のための貴重な情報を提供してくれます。

## ポートフォリオバックテストの実施と複数戦略の評価

ポートフォリオバックテストは、複数の戦略を同時に評価するための手法です。tradingviewのスクリプトエディターでは、ポートフォリオバックテストを行うことができます。ポートフォリオバックテストの実施方法と複数戦略の評価方法を解説します。

まず、複数の戦略を作成します。複数の戦略を作成する際には、各戦略のエントリーポイントとエグジットポイントを区別するために、識別子を設定することが重要です。また、各戦略のウェイト（割合）を設定することもできます。

次に、ポートフォリオバックテストの設定を行います。ポートフォリオバックテストの設定項目には、各戦略の資本配分やリバランスのタイミング、リバランスのルールなどがあります。これらの設定を行ってポートフォリオを作成します。

ポートフォリオバックテストの結果を詳細に分析し、各戦略のパフォーマンスを評価します。それぞれの戦略の収益率や勝率、リターンドローダウンなどを詳しく確認し、戦略の組み合わせやウェイトの調整などを行うことで、より良いポートフォリオを作成することができます。

以下にポートフォリオバックテストの実施と複数戦略の評価のサンプルコードを示します。

```pine
//@version=4
strategy("my strategy 1", overlay=true)

condition = crossover(sma(close, 14), sma(close, 28))

strategy.entry("long", strategy.long, when=condition)
strategy.exit("exit", "long")

//@version=4
strategy("my strategy 2", overlay=true)

condition = crossunder(sma(close, 14), sma(close, 28))

strategy.entry("short", strategy.short, when=condition)
strategy.exit("exit", "short")

// ポートフォリオバックテストの実施
portfolio = strategy.portfolio("my portfolio")

// 戦略1のウェイトを設定
strategy.weight("my strategy 1", portfolio, 0.5)

// 戦略2のウェイトを設定
strategy.weight("my strategy 2", portfolio, 0.5)

// ポートフォリオバックテストの結果を可視化
strategy.equity(portfolio, overlay=true)
plot(strategy.equity)
```

このサンプルコードでは、2つの戦略（strategy1とstrategy2）を作成しています。それぞれの戦略をポートフォリオに組み込むために、

　

## 【TradingView】関連のまとめ
https://hack-note.com/summary/tradingview-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

