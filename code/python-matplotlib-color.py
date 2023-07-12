## ```python
import matplotlib.pyplot as plt
import numpy as np

# データの作成
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# グラフの描画
plt.plot(x, y, color='red')

# グラフの表示
plt.show()
## ```


## ```python
import matplotlib.pyplot as plt
import numpy as np

# データの作成
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# グラフの描画
plt.plot(x, y, color=(0, 0, 1)) # 青色

# グラフの表示
plt.show()
## ```

