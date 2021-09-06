import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/park.jpg")
cv.imshow('Bonston', img)

# BRG to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

# hsv to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv_bgr", hsv_bgr)

# hsv to bgr
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("lab_bgr", lab_bgr)

plt.imshow(rgb)
plt.show()

# cv.waitKey(0)
