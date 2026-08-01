import cv2
import numpy as np

img = cv2.imread("picture.jpg")
img = cv2.resize(img, (400, 300))

# I.1 Độ sáng
bright = cv2.convertScaleAbs(img, alpha=1, beta=70)

# I.2 Độ tương phản
contrast = cv2.convertScaleAbs(img, alpha=2, beta=0)

# Ghép ảnh
result = np.hstack((img, bright, contrast))
cv2.imshow("Goc | Sang | Tuong phan", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
