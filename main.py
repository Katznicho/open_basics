import cv2 as cv

# read an image
# image = cv.imread("images/catone.jpeg")
# print(image)

# show image
# cv.imshow("Cat Imahe", image)


# reading videos

capture = cv.VideoCapture("videos/markdown.mp4")

# print("Enter the any letter to stop the video:")
# letter = input()
letter ='c'
while True:
    isTrue, frame = capture.read()
    cv.imshow("Mark down video", frame)

    # stop video from playing indefinitely
    if cv.waitKey(20) & 0xFF == ord(letter):
        break
capture.release()
cv.destroyAllWindows()

# add a specific delay
cv.waitKey(0)

# Resizing and rescaling images