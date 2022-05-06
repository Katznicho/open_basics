import cv2

cameraCapture = cv2.VideoCapture(0)

fps = 30  # an assumption of frames per second

size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'MyOutputVid.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),
    fps, size)
isTrue, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1
while isTrue and numFramesRemaining > 0:
    videoWriter.write(frame)
    isTrue, frame = cameraCapture.read()
    numFramesRemaining -= 1
cameraCapture.release()
