import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread("dong ruong.jpg")

# Kiểm tra ảnh
if image is None:
    print("Không tìm thấy ảnh!")
    exit()

# Tạo kernel làm sắc nét
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Áp dụng bộ lọc làm sắc nét
sharpen = cv2.filter2D(image, -1, kernel)

# Hiển thị ảnh
cv2.imshow("Anh goc", image)
cv2.imshow("Anh sau khi lam sac net", sharpen)

# Lưu ảnh kết quả
cv2.imwrite("sharpen.jpg", sharpen)

# Chờ nhấn phím để thoát
cv2.waitKey(0)
cv2.destroyAllWindows()