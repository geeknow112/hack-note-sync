## ```python
import matplotlib as mpl

mpl.rcParams['font.family'] = 'IPAexGothic'
## ```


## ```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 5, 20, 15, 30]
labels = ['りんご', 'みかん', 'ぶどう', 'バナナ', 'キウイ']

plt.bar(x, y, tick_label=labels)
plt.xlabel('フルーツ')
plt.ylabel('売上数')
plt.title('フルーツの売上数')
plt.show()
## ```

