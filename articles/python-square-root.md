【Python】ルートを求める方法
Python,ルート
python-square-root

こんにちは。今回は、Python初心者に向けて、ルートを求める方法について解説します。ルートとは、数値の平方根のことを指します。Pythonには、ルートを求めるための機能が標準で用意されています。

以下では、実際のコード例を交えて、ルートを求める方法について解説していきます。

## mathモジュールを使った方法

Pythonの標準ライブラリに含まれるmathモジュールを使うことで、ルートを求めることができます。mathモジュールのsqrt関数を使うことで、数値の平方根を求めることができます。

以下は、mathモジュールを使った例です。

```python
import math

# 2の平方根を求める
root = math.sqrt(2)
print(root)
```

出力結果は以下のようになります。

```
1.4142135623730951
```

## **演算子を使った方法

Pythonには、**演算子を使うことで、ルートを求める方法もあります。**演算子を使う場合、数値に対して「** 0.5」を計算することで、平方根を求めることができます。

以下は、**演算子を使った例です。

```python
# 2の平方根を求める
root = 2 ** 0.5
print(root)
```

出力結果は以下のようになります。

```
1.4142135623730951
```

## cmathモジュールを使った方法

cmathモジュールは、複素数を扱うためのモジュールです。cmathモジュールのsqrt関数を使うことで、虚数を含む数値の平方根を求めることができます。

以下は、cmathモジュールを使った例です。

```python
import cmath

# -1の平方根を求める
root = cmath.sqrt(-1)
print(root)
```

出力結果は以下のようになります。

```
1j
```

ここで、出力結果が「1j」となっているのは、-1の平方根が虚数単位i（jと同じ意味）を含む複素数であるためです。

以上で、Pythonでルートを求める方法について解説しました。それぞれの方法には、メリット・デメリットがありますので、目的に応じて使い分けることが大切です。

## まとめ

- Pythonには、mathモジュールを使った方法、**演算子を使った方法、cmathモジュールを使った方法がある。
- mathモジュールは、実数の平方根を求めることができる。
- **演算子は、実数の平方根を求めることができる。
- cmathモジュールは、虚数を含む数値の平方根を求めることができる。
- 目的に応じて、使い分けることが大切である。

以上が、Python初心者に向けたルートを求める方法の解説でした。

## データサイエンティストスクール 無料部分あります
PythonやRなどのプログラミングを学ぶなら、
さらに統計分野を学習してデータサイエンティストを目指すのがおすすめ！

ディープラーニングやビックデータ分析などの高額システム案件の受注にも有利になります。

システム開発より、分析がやりたい方向けですが、下記載せておきます。

https://hack-note.com/programming-schools/#toc17

　

## Python 関連のまとめ
https://hack-note.com/summary/python-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

