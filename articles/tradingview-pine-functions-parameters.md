【tradingview】pineスクリプト：関数の使用とパラメータ
tradingview,pine
tradingview-pine-functions-parameters

## tradingview pine scriptについて初心者エンジニアに向けて

こんにちは。今回は、tradingviewのpineスクリプトについて初心者エンジニア向けに解説します。

tradingviewは、株式市場や仮想通貨市場のチャートやテクニカル分析を行うためのwebベースのプラットフォームです。その中でもpineスクリプトは、チャート上に自動売買ロジックやカスタムインジケーターを作成するためのスクリプト言語です。

pineスクリプトを使えば、トレンドフォローや逆張りのストラテジーを自動化することができます。また、テクニカル分析でよく使用される移動平均線やボリンジャーバンドなどのインジケーターを自作することも可能です。

pineスクリプトでは、関数の使用とパラメータの設定が非常に重要です。関数は、特定のアクションを実行するための命令をまとめたものです。パラメータは、関数に渡す値のことで、関数の挙動を制御するために使用されます。

以下では、関数の定義と呼び出し方、パラメータの設定とデフォルト値、内部関数と外部関数の違い、関数の戻り値の活用方法、ビルトイン関数とカスタム関数の利用法について順番に解説していきます。


## 関数の定義と呼び出し方

関数は、特定のアクションを実行するための処理のまとまりです。pineスクリプトでは、関数を定義するためには`study`キーワードを使用します。以下に関数の定義と呼び出し方のサンプルコードを示します。

```pine
//@version=4
study(title="custom function example", shorttitle="custom function")

// 関数の定義
myfunction(p1, p2) =>
    p1 + p2

// 関数の呼び出し
result = myfunction(2, 3)
plot(result)
```

上記のコードでは、`myfunction`というカスタム関数を定義しています。この関数は、2つの引数(`p1`と`p2`)を受け取り、それらの値を加算して返します。`myfunction`は`result`という変数に格納された関数の戻り値として呼び出されており、最後に`plot`関数を使って`result`の値をチャート上に表示しています。


## パラメータの設定とデフォルト値

関数のパラメータは、関数に渡す値のことで、関数の挙動を制御するために使用されます。パラメータのデフォルト値を設定することで、必要に応じて引数を省略することができます。

以下にパラメータの設定とデフォルト値のサンプルコードを示します。

```pine
//@version=4
study(title="parameter default value example", shorttitle="parameter default value")

// 関数の定義
myfunction(p1, p2 = 0) =>
    p1 + p2

// 関数の呼び出し
result1 = myfunction(2)
result2 = myfunction(2, 3)
plot(result1, color=color.red)
plot(result2, color=color.blue)
```

上記のコードでは、`myfunction`関数の2つ目の引数`p2`にデフォルト値`0`を設定しています。引数を省略した場合、自動的にデフォルト値が適用されます。`result1`の計算では`p2`にデフォルト値が使用され、`result2`では引数として`3`が指定されています。

`plot`関数を使って`result1`と`result2`の値を赤と青でチャート上に表示しています。


## 内部関数と外部関数の違い

pineスクリプトでは、内部関数と外部関数の2つのタイプの関数が利用できます。内部関数は、pineスクリプトの中で定義され、他の関数内からのみ呼び出されます。一方、外部関数は、pineスクリプト外部から呼び出すことができます。

以下に内部関数と外部関数の違いを示すサンプルコードを示します。

```pine
//@version=4
study(title="internal and external function example", shorttitle="internal and external function")

// 内部関数の定義
internalfunction() =>
    // 内部関数の処理
    "internal function"

// 外部関数の定義
externalfunction() =>
    // 外部関数の処理
    "external function"

// 関数の呼び出し
internalresult = internalfunction()
externalresult = externalfunction()

plot(internalresult, color=color.red)
plot(externalresult, color=color.blue)
```

上記のコードでは、`internalfunction`と`externalfunction`という2つの関数を定義しています。`internalfunction`は内部関数であり、`externalfunction`は外部関数です。

`internalfunction`は、他の関数内からのみ呼び出すことができるため、この関数の戻り値を変数`internalresult`に格納してチャート上に表示しています。

一方、`externalfunction`は外部からも呼び出せる関数であり、この関数の戻り値を変数`externalresult`に格納してチャート上に表示しています。


## 関数の戻り値の活用方法

関数は、特定のアクションを実行して結果を戻すために使用されます。関数の戻り値は、他の関数内で利用したり、変数に格納して後で使うことができます。

以下に関数の戻り値の活用方法を示すサンプルコードを示します。

```pine
//@version=4
study(title="function return value example", shorttitle="function return value")

// 関数の定義
myfunction() =>
    // 関数の処理
    "hello, world!"

// 関数の呼び出し
result = myfunction()

// ラベルに関数の戻り値を表示
label.new(bar_index, high, text=result)
```

上記のコードでは、`myfunction`という関数を定義しています。この関数は、`hello, world!`というテキストを返します。

`myfunction`を呼び出し、その結果を変数`result`に格納しています。そして、`label.new`関数を使ってチャート上にラベルを表示し、そのテキストに関数の戻り値を表示しています。


## ビルトイン関数とカスタム関数の利用法

pineスクリプトでは、ビルトイン関数とカスタム関数の2つのタイプの関数を利用することができます。ビルトイン関数は、pineスクリプトに組み込まれている関数であり、データの演算やチャート描画などの一般的な操作を行うために使用されます。一方、カスタム関数はユーザーが独自に作成した関数であり、特定の目的に応じた処理を行うために使用されます。

以下にビルトイン関数とカスタム関数の利用法のサンプルコードを示します。

```pine
//@version=4
study(title="built-in and custom function example", shorttitle="built-in and custom function")

// カスタム関数の定義
myfunction(p1) =>
    // カスタム関数の処理
    p1 * ema(close, 14)

// ビルトイン関数の利用
builtinresult = sma(close, 14)

// カスタム関数の利用
customresult = myfunction(2)

plot(builtinresult, color=color.red)
plot(customresult, color=color.blue)
```

上記のコードでは、`myfunction`というカスタム関数を定義しています。この関数は、引数`p1`と終値データの指数移動平均線(ema)を乗算した値を返します。

また、ビルトイン関数の一つである`sma`関数も利用しています。`sma`関数は、終値データの単純移動平均線(sma)を計算するために使用されます。

`builtinresult`と`customresult`にそれぞれビルトイン関数とカスタム関数の結果を格納し、`plot`関数を使ってチャート上に表示しています。ビルトイン関数の結果は赤で表示し、カスタム関数の結果は青で表示しています。


## まとめ

以上で、tradingviewのpineスクリプトにおける関数の使用とパラメータの設定について解説しました。関数を使うことで、トレード戦略を自動化したり、カスタムインジケーターを作成したりすることが可能です。パラメータの設定や戻り値の活用方法も理解しておくと、効果的なpineスクリプトの作成ができるでしょう。

もしpineスクリプトの具体的な使い方やテクニカル分析の手法について知りたい場合は、下記のブログ記事を参考にしてください。

- 参考記事1：[tradingview公式ドキュメント](https://jp.tradingview.com/pine-script-docs/)
- 参考記事2：[pineスクリプトによるテクニカル分析の基本](https://www.example.com/blog/pine-script-tutorial)

tradingviewとpineスクリプトのさらなる理解とスキルアップのために、自分自身でコードを書いて実際に動かしてみることをおすすめします。初心者エンジニアでも、簡単な戦略やインジケーターから始めて徐々にスキルを高めていくことができるでしょう。

　

## 【TradingView】Pine Script関連のまとめ
https://hack-note.com/summary/tradingview-pine-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

