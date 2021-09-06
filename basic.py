import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Cat", img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("canny edges", canny)

# dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=5)
cv.imshow("dilated", dilated)

# eroding
eroded = cv.erode(dilated, (7, 7), iterations=1)
cv.imshow("eroded", eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resize", resized)

# cropping
cropped = img[50: 200, 200:400]
cv.imshow("cropped", cropped)

cv.waitKey(0)
