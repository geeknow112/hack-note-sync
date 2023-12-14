<!--
title: 【tradingview】pineスクリプトによるオーダーブロッカーの実装方法
tags: tradingview,pine
id: 
private: false
-->

## tradingview pine scriptについて初心者エンジニアに向けて、オーダーブロッカーの実装方法を解説します

こんにちは。今回は、tradingview pine scriptについて初心者エンジニアに向けて、オーダーブロッカーの実装方法について解説します。tradingview pine scriptは、トレーディングビューのチャート上にカスタムインジケーターやトレード戦略を記述するためのスクリプト言語です。オーダーブロッカーとは、特定の条件やルールに基づいてエントリーやエグジットを制御するための機能です。

トレードビューでカスタムインジケーターやトレード戦略を作成する際に、オーダーブロッカーを実装することで、自動的にエントリーやエグジットを制御することができます。これにより、トレーダーは感情的な判断やミスを防ぐことができるため、トレードの結果を改善することができるでしょう。

以下では、オーダーブロッカーの基本原理と概要から、具体的な実装方法までを解説します。

## オーダーブロッカーの基本原理と概要

オーダーブロッカーは、特定の条件やルールに基づいてエントリーやエグジットの実行を制御するための機能です。例えば、特定の指標が一定の値を超えた場合にのみエントリーを実行するといった制御が可能です。オーダーブロッカーは、if文や関数を使用してロジックを記述することができます。

以下に、基本的なオーダーブロッカーの構造を示します。

```pinescript
//@version=4
strategy("order blocker example")

// 条件式とルールの設定
entrycondition = close > open
exitcondition = close < open

// エントリーとエグジットの制御
if entrycondition
    strategy.entry("long", strategy.long)

if exitcondition
    strategy.close("long")
```

上記のコードでは、`entrycondition`と`exitcondition`という変数にエントリーやエグジットの条件式を設定しています。それぞれの条件式は、`close`が`open`よりも大きい場合に`true`となります。その後、`if`文を使用してエントリーやエグジットを制御しています。

## インジケーターを使用したオーダーブロッカーの実装

オーダーブロッカーには、トレードビューに組み込まれているインジケーターを使用することもできます。これにより、より高度な条件やルールを設定することができます。

以下に、移動平均線（ma）を使用したオーダーブロッカーの例を示します。

```pinescript
//@version=4
study("order blocker indicator example")

period = input(14, "period")
ma = sma(close, period)

// エントリーとエグジットの制御
entrycondition = close > ma
exitcondition = close < ma

// オーダーブロッカーのプロット
plotshape(entrycondition, style=shape.triangleup, color=color.green, size=size.small)
plotshape(exitcondition, style=shape.triangledown, color=color.red, size=size.small)
```

上記のコードでは、移動平均線（ma）を使用してエントリーやエグジットの条件式を設定しています。`entrycondition`は、`close`がmaよりも大きい場合に`true`となり、エントリーが実行されます。同様に、`exitcondition`は、`close`がmaよりも小さい場合に`true`となり、エグジットが実行されます。また、`plotshape`関数を使用して、エントリーやエグジットのポイントをプロットしています。

## 条件式とルールの設定方法

オーダーブロッカーでは、特定の条件式とルールを設定することで、エントリーやエグジットを制御します。条件式は、if文や論理演算子を使用して記述することができます。

以下に、条件式とルールの設定方法を示す例を示します。

```pinescript
//@version=4
strategy("order blocker example")

entrycondition = close > open and rsi(close, 14) > 70
exitcondition = close < open or rsi(close, 14) < 30

if entrycondition
    strategy.entry("long", strategy.long)

if exitcondition
    strategy.close("long")
```

上記のコードでは、`entrycondition`と`exitcondition`という変数に複数の条件式を設定しています。エントリーの条件として、`close`が`open`よりも大きく、rsi（14期間）が70よりも大きい場合にエントリーが実行されます。エグジットの条件として、`close`が`open`よりも小さいか、rsi（14期間）が30よりも小さい場合にエグジットが実行されます。

## エントリーとエグジットの制御方法

オーダーブロッカーでは、エントリーやエグジットの制御を自由に設定することができます。具体的なエントリーやエグジットの条件は、トレーダーの取引戦略や好みによって異なります。

以下に、エントリーやエグジットの制御方法の一例を示します。

```pinescript
//@version=4
strategy("order blocker example")

// エントリーの制御方法
if close > open
    strategy.entry("long", strategy.long)

if close < open
    strategy.entry("short", strategy.short)

// エグジットの制御方法
if close > high
    strategy.close("long")

if close < low
    strategy.close("short")
```

上記のコードでは、`close`が`open`よりも大きい場合にエントリーを実行し、`close`が`open`よりも小さい場合にショートポジションを実行しています。また、`close`が当日の高値を超えた場合には、ロングポジションをクローズし、`close`が当日の安値を下回った場合には、ショートポジションをクローズしています。

## バックテストと実際のトレードへの応用

オーダーブロッカーは、バックテストや実際のトレードでの応用も可能です。トレーディングビューのバックテスト機能を使用することで、過去のデータを使用してオーダーブロッカーの性能を評価することができます。

また、トレーディングビューのチャート画面上でオーダーブロッカーを使用することで、リアルタイムでエントリーやエグジットを制御することができます。これにより、トレーダーは自動的にトレードを行うことができるため、時間とエネルギーを節約することができます。

オーダーブロッカーを使用したトレード戦略やインジケーターは、チャート分析やテクニカル分析の道具の一つです。トレーディングビューのpineスクリプトを使用することで、トレーダーは自分自身の取引スタイルや戦略に合わせたカスタムインジケーターやオーダーブロッカーを作成することができます。

## まとめ

以上、tradingview pine scriptについて初心者エンジニアに向けたオーダーブロッカーの実装方法について解説しました。オーダーブロッカーは、特定の条件やルールに基づいてエントリーやエグジットを制御するための機能です。pineスクリプトを使用することで、トレーダーは自分自身の取引スタイルや戦略に合わせたカスタムインジケーターやオーダーブロッカーを作成することができます。

参考ブログ記事：
- [tradingviewのpine script入門](https://fintan.jp/?p=590)
- [tradingviewのpine scriptからのメール通知の実装方法](https://qiita.com/naoya_takahashi/items/3943ef0de68b200941b4)

## twitter関連のまとめ
https://hack-note.com/tools/twitter-summary/


## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

