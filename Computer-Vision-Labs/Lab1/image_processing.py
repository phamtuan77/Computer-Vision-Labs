import cv2
from PIL import Image
import os


# ==============================
# 1. ĐỌC VÀ HIỂN THỊ ẢNH
# ==============================

# Đường dẫn ảnh đầu vào
image_path = "picture.jpg"

# Đọc ảnh bằng OpenCV
image = cv2.imread(image_path)

# Kiểm tra ảnh có tồn tại không
if image is None:
    print("Không tìm thấy hình ảnh!")
    exit()

# Hiển thị ảnh gốc
cv2.imshow("Anh goc", image)

# Lưu ảnh sang định dạng khác
cv2.imwrite("output.png", image)

print("Đã đọc và lưu ảnh thành công!")


# ==============================
# 2. CHUYỂN ĐỔI KHÔNG GIAN MÀU
# ==============================

# OpenCV đọc ảnh theo BGR
# Chuyển từ BGR sang RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Chuyển sang Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Chuyển sang HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Chuyển sang LAB
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Hiển thị ảnh Grayscale
cv2.imshow("Grayscale", gray_image)

# Lưu ảnh Grayscale
cv2.imwrite("gray_image.jpg", gray_image)

# Lưu ảnh HSV
cv2.imwrite("hsv_image.jpg", hsv_image)

# Lưu ảnh LAB
cv2.imwrite("lab_image.jpg", lab_image)


# ==============================
# 3. CẮT XÉN ẢNH
# ==============================

# Lấy kích thước ảnh
height, width = image.shape[:2]

# Cắt vùng ảnh
# Cú pháp: image[y1:y2, x1:x2]
cropped_image = image[
    int(height * 0.25):int(height * 0.75),
    int(width * 0.25):int(width * 0.75)
]

# Hiển thị ảnh đã cắt
cv2.imshow("Anh da cat", cropped_image)

# Lưu ảnh đã cắt
cv2.imwrite("cropped_image.jpg", cropped_image)


# ==============================
# 4. THAY ĐỔI KÍCH THƯỚC
# ==============================

# Resize theo kích thước cố định
resized_fixed = cv2.resize(image, (800, 600))

# Resize theo tỷ lệ
scale = 0.5

resized_ratio = cv2.resize(
    image,
    None,
    fx=scale,
    fy=scale,
    interpolation=cv2.INTER_AREA
)

# Hiển thị ảnh resize
cv2.imshow("Resize 800x600", resized_fixed)
cv2.imshow("Resize 50%", resized_ratio)

# Lưu ảnh
cv2.imwrite("resized_fixed.jpg", resized_fixed)
cv2.imwrite("resized_ratio.jpg", resized_ratio)


# ==============================
# 5. VẼ HÌNH CƠ BẢN
# ==============================

# Tạo bản sao để vẽ
drawing_image = image.copy()

# Vẽ đường thẳng
cv2.line(
    drawing_image,
    (50, 50),
    (400, 50),
    (255, 0, 0),
    3
)

# Vẽ hình chữ nhật
cv2.rectangle(
    drawing_image,
    (100, 100),
    (400, 300),
    (0, 255, 0),
    3
)

# Vẽ hình tròn
cv2.circle(
    drawing_image,
    (600, 250),
    100,
    (0, 0, 255),
    3
)

# Thêm văn bản
cv2.putText(
    drawing_image,
    "OpenCV Image Processing",
    (100, 450),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

# Hiển thị ảnh đã vẽ
cv2.imshow("Anh ve hinh va van ban", drawing_image)

# Lưu ảnh
cv2.imwrite("drawing_image.jpg", drawing_image)


# ==============================
# SỬ DỤNG PILLOW
# ==============================

# Mở ảnh bằng Pillow
pil_image = Image.open(image_path)

# Hiển thị thông tin ảnh
print("\n===== THÔNG TIN ẢNH =====")
print("Tên file:", image_path)
print("Kích thước:", pil_image.size)
print("Định dạng:", pil_image.format)
print("Chế độ màu:", pil_image.mode)

# Chuyển ảnh sang RGB
pil_rgb = pil_image.convert("RGB")

# Chuyển ảnh sang Grayscale
pil_gray = pil_image.convert("L")

# Lưu ảnh bằng Pillow
pil_rgb.save("pillow_rgb.png")
pil_gray.save("pillow_grayscale.jpg")

print("\nĐã xử lý ảnh bằng Pillow thành công!")


# Chờ người dùng nhấn phím
cv2.waitKey(0)

# Đóng tất cả cửa sổ
cv2.destroyAllWindows()