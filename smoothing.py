import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow('cats', img)

# averaging
average = cv.blur(img, (7, 7))
cv.imshow("Average blur", average)

# gausian blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("gaussian", gauss)

# median
median = cv.medianBlur(img, 7)
cv.imshow("median", median)

# bilateral
bilatelar = cv.bilateralFilter(img,5,15,15)
cv.imshow("bilaterlar", bilatelar)

cv.waitKey(0)
