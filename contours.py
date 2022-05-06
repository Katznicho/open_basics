import cv2 as cv
import numpy as py

img =  cv.imread("images/catone.jpeg");
cv.imshow("Tiger Image",img)

#convert the image to gray scale
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale Image",img)

#find canny edges
canny = cv.Canny(img ,125,175)
cv.imshow("Canny Image", canny)

cv.waitKey(0)

