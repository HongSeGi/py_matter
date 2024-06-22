import numpy as np
import cv2

img = cv2.imread('image.jpg')

blur_bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# 회색조로 변환
gray_img = cv2.cvtColor(blur_bilateral, cv2.COLOR_BGR2GRAY)

# 인근 픽셀과 비교한 이진화
thresh = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 7)

cv2.imshow('original', img)
cv2.imshow('bilateral', blur_bilateral)
cv2.imshow('gray', gray_img)
cv2.imshow('binary', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

#오류 발생해서 다른방식으로 하기로 했다.