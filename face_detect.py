import cv2 as cv
import numpy as py


def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# img = cv.imread("Photos/group 1.jpg")
# cv.imshow("Person", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

img = cv.imread("Photos/IMG_0642.JPG")
cv.imshow("Person", rescaleFrame(img))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", rescaleFrame(gray))

haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=10)

print(f'number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

# cv.imshow("detected faces", img)

cv.imshow("detected faces", rescaleFrame(img))

cv.waitKey(0)
