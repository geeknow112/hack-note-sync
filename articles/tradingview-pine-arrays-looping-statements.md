【tradingview】pineスクリプト：配列とループ処理
tradingview,pine
tradingview-pine-arrays-looping-statements

## 【tradingview】pineスクリプト：配列とループ処理

こんにちは。今回は、tradingview pine scriptについて初心者エンジニアに向けて、配列とループ処理について解説します。

## 配列の作成と要素へのアクセス方法
まずは、配列の作成と要素へのアクセス方法についてご説明します。

pineスクリプトでは、配列は矩形のカッコ([])を使用して作成します。要素はインデックスを指定してアクセスすることができます。

以下は、配列の作成と要素へのアクセスのサンプルコードです。

```
//@version=4
study("pine script array - accessing elements", shorttitle="accessing elements")

// 配列の作成と要素へのアクセス方法
myarray = ["apple", "banana", "cherry", "durian"]

arrayelement1 = myarray[0]
arrayelement2 = myarray[1]
arrayelement3 = myarray[2]
arrayelement4 = myarray[3]

// 結果を出力
plot(arrayelement1, title="element 1")
plot(arrayelement2, title="element 2")
plot(arrayelement3, title="element 3")
plot(arrayelement4, title="element 4")
```

上記のコードでは、`myarray`という配列を作成し、その要素にアクセスしています。配列のインデックスは0から始まるため、`myarray[0]`は最初の要素を表し、`myarray[1]`は2番目の要素を表します。これを`plot()`関数を使用して表示しています。

## ループ処理の基本的な使い方
次に、pineスクリプトにおけるループ処理の基本的な使い方について解説します。

pineスクリプトでは、`for`キーワードを使用してループ処理を行います。`for`ループは、特定の条件を満たす間、あるいは特定の回数だけ処理を繰り返すことができます。

以下は、ループ処理の基本的な使い方を示したサンプルコードです。

```
//@version=4
study("pine script looping statements - basic usage", shorttitle="looping statements")

// ループ処理の基本的な使い方
for i = 1 to 5
    plot(i, title="loop index")
```

上記のコードでは、`for`ループを使用して1から5までの値を表示しています。`for`キーワードの後には、ループのカウンター変数（ここでは`i`）と、範囲（ここでは1から5）が指定されています。`plot()`関数を使用して、カウンター変数`i`を表示しています。

## forループと配列の要素処理
forループと配列の要素処理について解説します。

forループを使用することで、配列の要素を順番に処理することができます。

以下は、forループと配列の要素処理のサンプルコードです。

```
//@version=4
study("pine script for loop and array element processing", shorttitle="for loop and array element processing")

// forループと配列の要素処理
myarray = ["apple", "banana", "cherry", "durian"]

for i = 0 to (array.size(myarray) - 1)
    plot(myarray[i], title="array element")

```

上記のコードでは、`myarray`という配列を作成し、forループを使用して配列の要素を順番に表示しています。`array.size()`関数を使用して、配列の要素数を取得し、forループの終了条件として使用しています。`myarray[i]`を使用して、配列の`i`番目の要素を表示しています。

## 配列の要素の追加と削除の方法
配列の要素を追加と削除する方法について解説します。

pineスクリプトでは、配列に要素を追加するためには、`array.push()`関数を使用します。また、要素を削除するためには、`array.delete()`関数を使用します。

以下は、要素の追加と削除の方法を示したサンプルコードです。

```
//@version=4
study("pine script array - adding and deleting elements", shorttitle="adding and deleting elements")

// 配列の作成と要素の追加
myarray = ["apple", "banana", "cherry"]

array.push(myarray, "durian")

// 配列の要素の削除
array.delete(myarray, 1)

// 結果を出力
plot(myarray[0], title="element 1")
plot(myarray[1], title="element 2")
plot(myarray[2], title="element 3")
```

上記のコードでは、`array.push()`関数を使用して、`myarray`に要素を追加しています。また、`array.delete()`関数を使用して、`myarray`から要素を削除しています。最後に、`plot()`関数を使用して、変更後の配列の要素を表示しています。

## 配列の要素を活用するテクニック
最後に、配列の要素を活用するテクニックについて解説します。

配列の要素を活用することで、より柔軟な分析や条件の設定が可能になります。たとえば、複数の指標の値を配列に格納し、それらの値を比較して条件を判断することができます。

以下は、配列の要素を活用するテクニックを示したサンプルコードです。

```
//@version=4
study("pine script array - utilizing elements", shorttitle="utilizing elements")

// 配列の要素を活用するテクニック
smaarray = sma(close, 5)
emaarray = ema(close, 5)

for i = 0 to (array.size(smaarray) - 1)
    if smaarray[i] > emaarray[i]
        plotshape(close[i], style=shape.triangleup, color=color.green, title="buy signal")
    else if smaarray[i] < emaarray[i]
        plotshape(close[i], style=shape.triangledown, color=color.red, title="sell signal")
```

上記のコードでは、`sma()`関数と`ema()`関数を使用してそれぞれsmaとemaの値を計算し、配列に格納しています。forループを使用して、配列の要素を順番に比較し、条件に応じてシグナルを表示しています。

これは、2つの指標の交差点をシグナルとして表示している例ですが、配列の要素を活用することで、さまざまなテクニックを実装することができます。

以上が、tradingview pine scriptについて初心者エンジニアに向けた配列とループ処理の説明でした。

参考記事：
- [pine script tutorial: getting started guide](https://www.tradingview.com/blog/en/pine-script-tutorial-getting-started-guide-11199/)
- [pine script language reference manual](https://www.tradingview.com/pine-script-reference/v4/)

　

## 【TradingView】Pine Script関連のまとめ
https://hack-note.com/summary/tradingview-pine-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

