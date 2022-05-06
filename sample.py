import numpy
import cv2 as cv


def rescaleImage(frame, scale=0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture("videos/markdown.mp4")
print(capture)

# img = numpy.zeros((3, 3), type=numpy.uint8)
# new_rescaled_image = rescaleImage(img, 2.0)
# #new_rescaled_image[:] = [255, 255, 255]
# show = cv.imshow("White Image", new_rescaled_image)
# cv.waitKey(0)

# print(img)

# img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

# write  a new image
# new_image = cv.imwrite("images/new_image.png", img)
# new_image[0, 0] = [255, 255]
# print("done")
