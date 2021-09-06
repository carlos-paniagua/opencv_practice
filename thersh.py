import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

# blank = np.zeros(img.shape[:2], dtype="uint8")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("simple threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple threshold inv", thresh_inv)

# adaptive threshold
adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow("adaptive threshold", adaptive_threshold)

cv.waitKey(0)
