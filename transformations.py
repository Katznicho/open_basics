import cv2 as cv
img = cv.imread("images/catone.jpeg")
cv.imshow("Cat Image", img)

resized = cv.resize(img,(255,255))
cv.imshow("Resized", resized)
cv.waitKey(0)
