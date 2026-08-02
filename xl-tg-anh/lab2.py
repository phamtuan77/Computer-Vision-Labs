import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Đọc ảnh xám
img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

# 2. Biến đổi âm bản (Negative)
negative_img = 255 - img

# 3. Cắt ngưỡng (Thresholding)
_, thresh_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# --- HIỂN THỊ 3 ẢNH TRÊN CÙNG 1 HÀNG ---
# Đổi kích thước khung hình cho vừa vặn với 3 ảnh (10x4)
plt.figure(figsize=(10, 4))

images = [img, negative_img, thresh_img]
titles = ['1. Anh Goc', '2. Am Ban', '3. Cat Nguong']

# Sửa range(5) thành range(len(images)) -> Tự động chạy đúng số lượng ảnh (3 ảnh)
for i in range(len(images)):
    plt.subplot(1, 3, i + 1)  # Đổi thành (1, 3) để chia vừa đủ 3 cột
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i], fontsize=10)
    plt.axis('off')

plt.tight_layout()
plt.show()