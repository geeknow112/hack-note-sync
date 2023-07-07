# ```python
import numpy as np

# 2x2の行列を作成する
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 行列の積を計算する
c = np.dot(a, b)

print(c)
# ```


# ```python
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('data.csv')

# データの先頭5行を表示する
print(df.head())
# ```


# ```python
import matplotlib.pyplot as plt

# データを作成する
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 折れ線グラフを描画する
plt.plot(x, y)

# グラフを表示する
plt.show()
# ```


# ```python
from sklearn.linear_model import LinearRegression

# データを作成する
x = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# 線形回帰モデルを構築する
model = LinearRegression()
model.fit(x, y)

# モデルを使って予測する
pred = model.predict([[6]])

print(pred)
# ```
