import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('image.jpg')

blur_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# 회색조로 변환
gray_img = cv2.cvtColor(blur_bilateral, cv2.COLOR_BGR2GRAY)

# 인근 픽셀과 비교한 이진화
thresh = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 7)

#결과 임지출력
images = [img, blur_bilateral, gray_img, thresh]
titles = ['Original', "Bilarteral", "Gray", "Binary"]

plt.figure(figsize = (10, 8))
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB) if i == 0 else images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()