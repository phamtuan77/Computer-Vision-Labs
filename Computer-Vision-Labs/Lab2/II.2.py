import cv2

# Đọc ảnh
image = cv2.imread("phong canh.jpg")

# Kiểm tra ảnh có đọc được không
if image is None:
    print("Không tìm thấy ảnh!")
    exit()

# Lọc Gaussian
gaussian = cv2.GaussianBlur(image, (5, 5), 0)

# Hiển thị ảnh
cv2.imshow("Anh goc", image)
cv2.imshow("Gaussian Blur", gaussian)

# Lưu ảnh
cv2.imwrite("gaussian_blur.jpg", gaussian)

# Đợi nhấn phím để đóng cửa sổ
cv2.waitKey(0)
cv2.destroyAllWindows()