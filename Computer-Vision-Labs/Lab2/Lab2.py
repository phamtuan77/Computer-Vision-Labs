from pyexpat import features

import cv2
import numpy as np
from scipy import io

img = cv2.imread("picture.jpg")
img = cv2.resize(img, (400, 300))

# I.1 Cộng điểm ảnh (tăng sáng)
bright = np.clip(img.astype(int) + 80, 0, 255).astype(np.uint8)

# I.2 Nhân điểm ảnh (tăng tương phản)
contrast = np.clip(img.astype(float) * 1.8, 0, 255).astype(np.uint8)

result = np.hstack((img, bright, contrast))

cv2.imshow("Original | Brightness | Contrast", result)

cv2.waitKey(0)
cv2.destroyAllWindows()


#II.1
#OpenCV
image_path = 'vanmieu.jpg'
img_cv2 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
edges_cv2 = cv2.Canny(img_cv2, 100, 200)
#Scikit-image
img_skimage = io.imread(image_path, as_gray=True)
edges_skimage = features.canny(img_skimage, sigma=1.0)