import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Đọc ảnh từ file
img_path = "D:/Xu_Ly_Anh/Computer-Vision-Labs/Computer-Vision-Labs/Lab2/vanmieu.jpg" 
# Đọc trực tiếp dưới dạng ảnh xám (Grayscale)
img_cv2 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

if img_cv2 is None:
    print("Không tìm thấy ảnh! Hãy kiểm tra lại đường dẫn.")
else:

    # 2. Phát hiện cạnh bằng SOBEL
    
    sobelx = cv2.Sobel(img_cv2, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img_cv2, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.convertScaleAbs(cv2.magnitude(sobelx, sobely))

    # 3. Phát hiện cạnh bằng PREWITT

    prewitt_kernel_x = np.array([[-1, 0, 1], 
                                 [-1, 0, 1], 
                                 [-1, 0, 1]])
    
    prewitt_kernel_y = np.array([[-1, -1, -1], 
                                 [ 0,  0,  0], 
                                 [ 1,  1,  1]])
    
    prewitt_x = cv2.filter2D(img_cv2, -1, prewitt_kernel_x)
    prewitt_y = cv2.filter2D(img_cv2, -1, prewitt_kernel_y)
    
    prewitt_combined = cv2.addWeighted(cv2.convertScaleAbs(prewitt_x), 0.5, cv2.convertScaleAbs(prewitt_y), 0.5, 0)

    # 4. Hiển thị so sách kết quả bằng MATPLOTLIB
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(img_cv2, cmap='gray')
    plt.title('Ảnh gốc (Grayscale)')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(sobel_combined, cmap='gray')
    plt.title('Phát hiện cạnh - Sobel')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(prewitt_combined, cmap='gray')
    plt.title('Phát hiện cạnh - Prewitt')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()