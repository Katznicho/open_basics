import numpy as py
import cv2 as cv

img = py.zeros((500,500,3), dtype="uint8")
#img[100:400 , 50:80 ] = 255,255,255
blank_image =  cv.imshow("Blank Image", img)

# write text here
cv.putText(img,"KATENDE NICHOLAS",(100,250), cv.FONT_HERSHEY_PLAIN,2.0, (255,255,255), thickness=4)
cv.imshow("Text Image", img)

cv.waitKey(0)