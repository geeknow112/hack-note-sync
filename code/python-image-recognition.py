# ```python
import cv2

# 画像の読み込み
img = cv2.imread('sample.jpg')

# 画像の表示
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ```


# ```python
from PIL import Image

# 画像の読み込み
img = Image.open('sample.jpg')

# 画像のリサイズ
resized_img = img.resize((500, 500))

# リサイズした画像の保存
resized_img.save('resized_sample.jpg')
# ```
