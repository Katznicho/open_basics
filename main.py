import cv2 as cv

image = cv.imread("images/splash.png")
# print(image)

# show image
cv.imshow("My Image", image)
cv.waitKey(6000)
#cv.destroyWindow()
