import cv2
from PIL import Image

# Đọc ảnh

image_path = "picture.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Không tìm thấy ảnh!")
    exit()

cv2.imshow("Ảnh gốc", img)
cv2.imwrite("output.png", img)

print("Đã đọc và lưu ảnh thành công!")

# Chuyển đổi màu

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.imshow("Grayscale", gray)

cv2.imwrite("gray.jpg", gray)
cv2.imwrite("hsv.jpg", hsv)
cv2.imwrite("lab.jpg", lab)

# Cắt ảnh

h, w = img.shape[:2]

crop = img[
    int(h * 0.25):int(h * 0.75),
    int(w * 0.25):int(w * 0.75)
]

cv2.imshow("Ảnh cắt", crop)
cv2.imwrite("crop.jpg", crop)

# Resize

resize1 = cv2.resize(img, (800, 600))

resize2 = cv2.resize(
    img,
    None,
    fx=0.5,
    fy=0.5,
    interpolation=cv2.INTER_AREA
)

cv2.imshow("Resize 800x600", resize1)
cv2.imshow("Resize 50%", resize2)

cv2.imwrite("resize1.jpg", resize1)
cv2.imwrite("resize2.jpg", resize2)

# Vẽ hình

draw = img.copy()

cv2.line(draw, (50, 50), (400, 50), (255, 0, 0), 3)

cv2.rectangle(draw, (100, 100), (400, 300), (0, 255, 0), 3)

cv2.circle(draw, (600, 250), 100, (0, 0, 255), 3)

cv2.putText(
    draw,
    "OpenCV",
    (120, 450),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

cv2.imshow("Vẽ hình", draw)
cv2.imwrite("drawing.jpg", draw)

# Pillow

pil = Image.open(image_path)

print("\nTHÔNG TIN ẢNH")
print("Tên:", image_path)
print("Kích thước:", pil.size)
print("Định dạng:", pil.format)
print("Chế độ:", pil.mode)

pil.convert("RGB").save("pillow_rgb.png")
pil.convert("L").save("pillow_gray.jpg")

print("\nĐã xử lý xong!")

cv2.waitKey(0)
cv2.destroyAllWindows()
