import cv2
import time
import matplotlib.pyplot as plt

# Đọc ảnh
img = cv2.imread('lambo.jpg')

# Chuyển đổi từ BGR (OpenCV mặc định) sang RGB để hiển thị chính xác với matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Áp dụng bilateral filter
start_time = time.time()
result = cv2.bilateralFilter(img, 9, 75, 75)
end_time = time.time()

# Chuyển đổi kết quả filter sang RGB để hiển thị
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# In thời gian chạy
print("Time taken for bilateral filter:", end_time - start_time)

# Hiển thị ảnh mẫu và ảnh sau khi áp dụng bilateral filter
plt.figure(figsize=(10, 5))

# Hiển thị ảnh mẫu
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Hiển thị ảnh sau khi filter
plt.subplot(1, 2, 2)
plt.imshow(result_rgb)
plt.title("Filtered Image")
plt.axis('off')

plt.show()
