import cv2 as cv

catIMage = cv.imread("images/cattwo.jpeg")

# show image
mycat = cv.imshow('Cat Image', catIMage)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture("videos/markdown.mp4")

# print("Enter the any letter to stop the video:")
# letter = input()
letter = 'c'
while True:
    isTrue, frame = capture.read()

    resized_frame = rescaleFrame(frame, scale = 0.20)
    cv.imshow("Mark down video", resized_frame)

    # stop video from playing indefinitely
    if cv.waitKey(20) & 0xFF == ord(letter):
        break
capture.release()
cv.destroyAllWindows()
# await key
cv.waitKey(0)
