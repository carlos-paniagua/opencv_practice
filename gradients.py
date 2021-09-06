import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos/park.jpg")
cv.imshow("Cats", img)

# blank = np.zeros(img.shape[:2], dtype="uint8")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian",lap)

#sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow("sobelx", sobelx)
cv.imshow("sobely", sobely)
cv.imshow("combined_sobel", combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow("canny",canny)

cv.waitKey(0)
