import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank",blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("blur", blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow("canny edges", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

contours, hireachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contours, hireachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# contours, hireachies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# contours, hireachies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours Drawn",blank)

cv.waitKey(0)
