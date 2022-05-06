import cv2 as cv
import numpy as py

img = cv.imread('images/catone.jpeg')
cv.imshow("Tiger Image", img)
b, g, r = cv.split(img)
cv.imshow("Blue", b)
cv.imshow("Green",g)
cv.imshow("Red", r)

print(f'The colors are {b} and {g} and {r}')

cv.waitKey(0)
