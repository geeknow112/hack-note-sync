【google colaboratory】入門：データの読み込みと前処理の基本
google,colaboratory,python
gcolab-data-processing

## 【google colaboratory】入門：データの読み込みと前処理の基本

こんにちは。今回は、google colaboratoryについて初心者エンジニアに向けて、データの読み込みと前処理の基本について解説します。

データの種類：csv、excel、json、sqlなど
---

データ分析や機械学習において、データの読み込みは非常に重要です。google colaboratory（以下、colab）を使えば、さまざまな形式のデータを簡単に読み込むことができます。主なデータの形式には、csv形式、excel形式、json形式、sql形式などがあります。

### csv形式のデータの読み込み例

まずは、csv形式のデータの読み込み方法を見ていきましょう。以下のコードをcolabのセルに記述して実行してください。

```python
import pandas as pd

# データの読み込み
data = pd.read_csv('data.csv')

# データの確認
print(data.head())
```

上記のコードでは、pandasライブラリを使用してcsv形式のデータを読み込んでいます。`read_csv`関数には読み込むファイルのパスを指定します。`head`関数を使うことで、最初の5行のデータを表示することができます。

### excel形式のデータの読み込み例

次に、excel形式のデータの読み込み方法を見ていきましょう。以下のコードをcolabのセルに記述して実行してください。

```python
import pandas as pd

# データの読み込み
data = pd.read_excel('data.xlsx')

# データの確認
print(data.head())
```

上記のコードでは、`read_excel`関数を使用してexcel形式のデータを読み込んでいます。`read_csv`関数と同様に、読み込むファイルのパスを指定します。

その他のデータ形式に関しても、pandasライブラリには対応している関数が用意されていますので、適宜使用してください。

データの前処理方法：欠損値、重複、異常値の処理
---

データの前処理はデータ分析の重要なステップです。ここでは、欠損値、重複、異常値の処理方法について見ていきましょう。

### 欠損値の処理

欠損値とは、データにおいて一部の値が欠けていることを指します。これらの欠損値は、分析結果に大きな影響を与える場合があります。以下のコードを使用して、欠損値を処理する方法を見ていきましょう。

```python
import pandas as pd

# データの読み込み
data = pd.read_csv('data.csv')

# 欠損値の確認
print(data.isnull().sum())

# 欠損値の削除
data = data.dropna()

# 欠損値の補完
data = data.fillna(0)
```

欠損値の確認には、`isnull()`関数を使用します。`isnull()`関数は、各要素が欠損値であるかどうかを判定し、trueまたはfalseを返します。`sum()`関数を用いれば、欠損値の合計を求めることができます。

欠損値の削除には、`dropna()`関数を使用します。`dropna()`関数は、欠損値を含む行を削除します。

欠損値の補完には、`fillna()`関数を使用します。`fillna()`関数には補完する値を指定します。上記の例では、欠損値を0で補完していますが、適切な値や平均値などを指定することもできます。

### 重複の削除

データには、重複した行が含まれる場合があります。重複を削除することで、分析の正確性を向上させることができます。以下のコードを使用して、重複した行を削除する方法を見ていきましょう。

```python
import pandas as pd

# データの読み込み
data = pd.read_csv('data.csv')

# 重複の確認
print(data.duplicated().sum())

# 重複の削除
data = data.drop_duplicates()
```

重複の確認には、`duplicated()`関数を使用します。`duplicated()`関数は、各行が重複しているかどうかを判定し、trueまたはfalseを返します。`sum()`関数を用いれば、重複した行の合計数を求めることができます。

重複の削除には、`drop_duplicates()`関数を使用します。`drop_duplicates()`関数は、重複した行を削除します。

### 異常値の処理

異常値とは、データの中で非常に大きな値や小さな値など、データのパターンから外れた値のことを指します。異常値は、データ分析の結果に歪みを与える可能性があるため、適切な処理を行う必要があります。以下のコードを使用して、異常値を処理する方法を見ていきましょう。

```python
import pandas as pd
import numpy as np

# データの読み込み
data = pd.read_csv('data.csv')

# 異常値の検出
mean = np.mean(data['column_name'])
std = np.std(data['column_name'])
threshold = mean + std * 3
outliers = data[data['column_name'] > threshold]

# 異常値の削除
data = data[data['column_name'] <= threshold]
```

異常値の検出には、統計的な手法を用いることが一般的です。上記の例では、平均値と標準偏差を使用して異常値の閾値を計算し、その閾値を超える値を異常値として検出しています。

異常値の削除には、異常値を含む行を取り除く方法を使用します。上記の例では、異常値を含む行を除外しています。

データの加工方法：列の追加、削除、変換
---

データの加工は、分析や機械学習の前処理において必要な作業です。ここでは、列の追加、削除、変換の方法について見ていきましょう。

### 列の追加

データに新しい列を追加することで、分析や機械学習のための特徴量を作成することができます。以下のコードを使用して、列の追加方法を見ていきましょう。

```python
import pandas as pd

# データの読み込み
data = pd.read_csv('data.csv')

# 新しい列の追加
data['new_column'] = data['column1'] + data['column2']
```

新しい列を追加するには、`dataframe`オブジェクトに対して新しい列を定義し、値を代入します。上記の例では、`column1`と`column2`の値を足して、`new_column`に代入しています。

### 列の削除

不要な列を削除することで、データのサイズを小さくすることができます。以下のコードを使用して、列の削除方法を見ていきましょう。

```python
import pandas as pd

# データの読み込み
data = pd.read_csv('data.csv')

# 列の削除
data = data.drop(['column1', 'column2'], axis=1)
```

列の削除には、`drop()`関数を使用します。`drop()`関数には削除する列名と`axis=1`のオプションを指定します。上記の例では、`column1`と`column2`を削除しています。

### 列の変換

データの列を変換することで、分析や機械学習のための特徴量を作成したり、データの形式を変更することができます。以下のコードを使用して、列の変換方法を見ていきましょう。

```python
import pandas as pd

# データの読み込み
data = pd.read_csv('data.csv')

# 列の変換
data['column1'] = data['column1'].apply(lambda x: x * 2)
data['column2'] = data['column2'].apply(lambda x: 'negative' if x < 0 else 'positive')
```

列の変換には、`apply()`関数を使用します。`apply()`関数には変換処理を定義する関数やラムダ式を指定します。

上記の例では、`column1`の各要素を2倍にしています。また、`column2`の各要素に対して条件式を適用し、値が負の場合は'negative'、それ以外の場合は'positive'という値に変換しています。

データの集計方法：pandasを使った集計方法
---

データの集計は、データ分析や機械学習において重要な作業です。ここでは、pandasを使った集計方法について見ていきましょう。

### 集計方法

pandasには、データの集計を行うための便利な関数やメソッドが用意されています。

#### 平均値の算出

平均値は、データの中の値の平均を求める統計量です。以下のコードを使用して、平均値を算出する方法を見ていきましょう。

```python
import pandas as pd

# データの読み込み
data = pd.read_csv('data.csv')

# 平均値の算出
mean = data['column_name'].mean()
print(mean)
```

`mean()`関数を使用して平均値を算出します。`mean()`関数は、`series`オブジェクトに対して使用することができ、各要素の平均値を返します。

#### 合計値の算出

合計値は、データの中の値の合計を求める統計量です。以下のコードを使用して、合計値を算出する方法を見ていきましょう。

```python
import pandas as pd

# データの読み込み
data = pd.read_csv('data.csv')

# 合計値の算出
total = data['column_name'].sum()
print(total)
```

`sum()`関数を使用して合計値を算出します。`sum()`関数は、`series`オブジェクトに対して使用することができ、各要素の合計値を返します。

#### 最小値と最大値の算出

最小値と最大値は、データの中の最も小さい値と最も大きな値を求める統計量です。以下のコードを使用して、最小値と最大値を算出する方法を見ていきましょう。

```python
import pandas as pd

# データの読み込み
data = pd.read_csv('data.csv')

# 最小値と最大値の算出
min_value = data['column_name'].min()
max_value = data['column_name'].max()
print(min_value, max_value)
```

`min()`関数と`max()`関数を使用して最小値と最大値を算出します。`min()`関数は最小値を、`max()`関数は最大値を返します。

### グループ化と集計

複数の要素でグループ化して集計することで、特定の属性に関連した集計結果を取得することができます。以下のコードを使用して、グループ化して集計する方法を見ていきましょう。

```python
import pandas as pd

# データの読み込み
data = pd.read_csv('data.csv')

# グループ化と集計
grouped_data = data.groupby('column_name').mean()
print(grouped_data)
```

`groupby()`関数を使用してグループ化を行います。グループ化する列を`groupby()`関数に指定します。`mean()`関数を使用することで、各グループの平均値を算出します。

データの可視化方法：matplotlibを使ったグラフの描画
---


　

## 【Google Colaboratory】まとめ
https://hack-note.com/summary/gcolab-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)


