## ```python
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cmap = cm.get_cmap('jet')
## ```


## ```python
import numpy as np

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)
## ```


## ```python
plt.imshow(Z, cmap=cmap)
plt.colorbar()
plt.show()
## ```

