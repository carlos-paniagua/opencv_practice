import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("circle", circle)

# bitwize and > intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwize_and", bitwise_and)

# bitwize or > non intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwize_or", bitwise_or)

# bitwize xor > non intersecting and intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwize_xor", bitwise_xor)

# bitwize not
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwize_not", bitwise_not)

cv.waitKey(0)
